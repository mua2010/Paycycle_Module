# Standard Library Imports
from datetime import (
    date as date_class, 
    timedelta
)

# Local Imports
from enums import WeekPlaceholder


def get_valid_date(holiday: date_class) -> date_class:
    """Given a holiday, return the nearest weekday that is not a holiday.
    """
    if not holiday:
        raise RuntimeError('No date passed in. A date is required to get a valid payday.')
    if not isinstance(holiday, date_class):
        raise RuntimeError('A date class object was not passed.')

    # for a weekday, placeholder for Monday is 0 and Sunday is 6

    num_of_days_after_holiday = 1
    week_day_placeholder = (holiday + timedelta(days=num_of_days_after_holiday)).weekday()
    while week_day_placeholder in {5,6}:
        num_of_days_after_holiday += 1
        week_day_placeholder = (holiday + timedelta(days=num_of_days_after_holiday)).weekday()
        
    num_of_days_before_holiday = 1
    week_day_placeholder = (holiday - timedelta(days=num_of_days_before_holiday)).weekday()
    while week_day_placeholder in {5,6}:
        num_of_days_before_holiday += 1
        week_day_placeholder = (holiday - timedelta(days=num_of_days_before_holiday)).weekday()

    # POST PROCESS
    # Note: If the number of days before and after are same, the default date will be next day.
    if num_of_days_before_holiday < num_of_days_after_holiday:
        return holiday - timedelta(days=num_of_days_before_holiday)
    else:
        return holiday + timedelta(days=num_of_days_after_holiday)


def get_nearest_payday(
        date: date_class,
        frequency: timedelta,
        holidays: list,
        payday: date_class,
        default_payday: WeekPlaceholder) -> date_class:
    """Leverage the given constraints to calculate a payday that is nearest
       to 'date'.
    """
    holiday = None
    
    def __get_respective_payday(_payday, _frequency):
        nonlocal holiday
        if _payday.weekday() != default_payday.value:
            # reset the payday to follow its original pay cycle
            _payday = holiday

        # If we land on a payday that is a holiday, we need to get a valid 
        # payday. The valid payday could be the the very next day or
        # the previous day (if the next weekday is a Monday)
        if (holiday := (_payday + _frequency)) in holidays:
            _payday = get_valid_date(holiday)
        else:
            _payday += _frequency
        return _payday

    # holiday = None
    if date < payday:
        # Go Backward

        # change frequency to negative
        frequency = timedelta(days=-1*frequency.days)

        while (payday > date):
            payday = __get_respective_payday(_payday=payday, _frequency=frequency)
            # if payday.weekday() != default_payday.value:
            #     # reset the payday to follow its original pay cycle
            #     payday = holiday

            # # If we land on a payday that is a holiday, we need to get a valid 
            # # payday. The valid payday could be the the very next day or
            # # the previous day (if the next weekday is a Monday)
            # if (holiday := (payday - frequency)) in holidays:
            #     payday = get_valid_date(holiday)
            # else:
            #     payday -= frequency
    else: 
        # Go Forward
        while (payday < date):
            payday = __get_respective_payday(_payday=payday, _frequency=frequency)
            # if payday.weekday() != default_payday.value:
            #     # reset the payday to follow its original pay cycle
            #     payday = holiday

            # # If we land on a payday that is a holiday, we need to get a valid 
            # # payday. The valid payday could be the the very next day or
            # # the previous day (if the next weekday is a Monday)
            # if (holiday := (payday + frequency)) in holidays:
            #     payday = get_valid_date(holiday)
            # else:
            #     payday += frequency

    return payday
