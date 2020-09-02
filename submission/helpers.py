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
    
def update_payday(
        payday: date_class,
        frequency: timedelta,
        holidays: list,
        default_payday: date_class):
    """Adds frequency to the payday and updates the payday by leveraging
       the given holidays and default_payday.
    """
    if payday.weekday() != default_payday.value:
        offset = default_payday.value - payday.weekday()
        payday += timedelta(days=offset)
        
    payday += frequency

    # keep finding a valid payday
    if payday in holidays:
        payday = get_valid_business_day(payday, holidays)
    
    return payday

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
        
    if date < given_payday:  # Go Backward
        # change frequency to negative
        frequency = timedelta(days=-1*frequency.days)
        while (_payday > date):
            _payday = update_payday(
                payday=_payday,
                frequency=frequency,
                holidays=holidays,
                default_payday=default_payday
            )
    else: # Go Forward
        while (_payday < date):
            _payday = update_payday(
                payday=_payday,
                frequency=frequency,
                holidays=holidays,
                default_payday=default_payday
            )
            
    return _payday
