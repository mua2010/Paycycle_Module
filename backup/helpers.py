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

def pick_nearest_date(
        date: date_class, 
        first_date: date_class, 
        second_date: date_class) -> date_class:
    """Return the first_date or second_date which ever is closer to 'date'.
    """
    if not (date or first_date or second_date):
        raise RuntimeError('No date passed in.')
    if not (isinstance(date, date_class)
            or isinstance(first_date, date_class)
            or isinstance(second_date, date_class)):
        raise RuntimeError('A date class object was not passed.')

    num_of_days_to_first_date = abs((date - first_date).days)
    num_of_days_to_second_date = abs((date - second_date).days)

    if num_of_days_to_first_date < num_of_days_to_second_date:
        return first_date
    else:
        return second_date

def get_nearest_payday(
        date: date_class,
        frequency: timedelta,
        holidays: list,
        nearest_given_payday: date_class,
        default_payday: WeekPlaceholder) -> date_class:
    """Leverage the given constraints to calculate a payday that is nearest
       to 'date'.
    """
    holiday = None
    nearest_payday = nearest_given_payday
    if date < nearest_payday:
        # Go Backward
        while (nearest_payday > date):
            if nearest_payday.weekday() != default_payday.value:
                # reset the nearest_payday to follow its original pay cycle
                nearest_payday = holiday

            if (holiday := (nearest_payday - frequency)) in holidays:
                nearest_payday = get_valid_date(holiday)
            else:
                nearest_payday -= frequency
    else: 
        # Go Forward
        while (nearest_payday < date):
            if nearest_payday.weekday() != default_payday.value:
                # reset the nearest_payday to follow its original pay cycle
                nearest_payday = holiday

            if (holiday := (nearest_payday + frequency)) in holidays:
                nearest_payday = get_valid_date(holiday)
            else:
                nearest_payday += frequency

    return nearest_payday
