# Standard Library Imports
from datetime import (
    date as date_class, 
    timedelta
)

# Local Imports
from enums import WeekPlaceholder


def get_valid_business_day(date: date_class, holidays) -> date_class:
    """Given a date, return the nearest business day that could be a
       potential payday.
       Note: For the days in a week, placeholder for Monday is 0 and Sunday is 6
    """
    
    while date in holidays:
        num_of_days_after_holiday = 1
        week_day_placeholder = (date + timedelta(days=num_of_days_after_holiday)).weekday()
        while week_day_placeholder in {5,6}:
            num_of_days_after_holiday += 1
            week_day_placeholder = (date + timedelta(days=num_of_days_after_holiday)).weekday()
            
        num_of_days_before_holiday = 1
        week_day_placeholder = (date - timedelta(days=num_of_days_before_holiday)).weekday()
        while week_day_placeholder in {5,6}:
            num_of_days_before_holiday += 1
            week_day_placeholder = (date - timedelta(days=num_of_days_before_holiday)).weekday()

        # POST PROCESS
        # Note: If the number of days before and after are same, the default date will be next day.
        if num_of_days_before_holiday < num_of_days_after_holiday:
            date -= timedelta(days=num_of_days_before_holiday)
        else:
            date += timedelta(days=num_of_days_after_holiday)
    return date
    


def get_nearest_payday(
        date: date_class,
        frequency: timedelta,
        holidays: list,
        given_payday: date_class,
        default_payday: WeekPlaceholder) -> date_class:
    """Leverage the given constraints to calculate a payday that is nearest
       to 'date'.
    """
    _payday = given_payday

    def __update_payday( _frequency: timedelta):
        nonlocal _payday

        if _payday.weekday() != default_payday.value:
            offset = default_payday.value - _payday.weekday()
            _payday += timedelta(days=offset)
            
        _payday += _frequency

        # keep finding a valid payday
        if _payday in holidays:
            _payday = get_valid_business_day(_payday, holidays)
        
    if date < given_payday:  # Go Backward
        # change frequency to negative
        frequency = timedelta(days=-1*frequency.days)
        while (_payday > date):
            __update_payday(_frequency=frequency)
    else: # Go Forward
        while (_payday < date):
            __update_payday(_frequency=frequency)

    return _payday
