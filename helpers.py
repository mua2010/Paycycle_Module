# Standard Library Imports
from datetime import (
    date as date_class, 
    timedelta
)


def get_valid_payday(holiday: date_class) -> date_class:
    """Calculates the neareast available payday which is a valid weekday.
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
    if num_of_days_before_holiday < num_of_days_after_holiday:
        return holiday - timedelta(days=num_of_days_before_holiday)
    else:
        return holiday + timedelta(days=num_of_days_after_holiday)

def pick_nearest_payday(
        date: date_class, 
        first_payday: date_class, 
        last_payday: date_class) -> date_class:
    """Returns the payday that is closer to date.
    """
    if not (date or first_payday or last_payday):
        raise RuntimeError('No date passed in.')
    if not (isinstance(date, date_class)
            or isinstance(first_payday, date_class)
            or isinstance(last_payday, date_class)):
        raise RuntimeError('A date class object was not passed.')

    num_of_days_to_first_payday = abs((date - first_payday).days)
    num_of_days_to_last_payday = abs((date - last_payday).days)

    if num_of_days_to_first_payday < num_of_days_to_last_payday:
        return first_payday
    else:
        return last_payday

def is_payday_helper(
        date: date_class, 
        frequency: timedelta,
        curr_day: date_class, default_payday: date_class, 
        holidays: list) -> bool:
    """A Helper function for PayCycle.is_payday.
       Leverges the provided config parameters
    """
    if date < curr_day:
        # Go Backward
        while (curr_day >= date):
            if curr_day == date:
                return True
            if curr_day.weekday() != default_payday:
                # reset the curr_day to follow its original pay cycle
                curr_day = holiday

            if (holiday := (curr_day - frequency)) in holidays:
                curr_day = get_valid_payday(holiday)
            else:
                curr_day -= frequency
        return False
    else: 
        # Go Forward
        while (curr_day <= date):
            if curr_day == date:
                return True
            if curr_day.weekday() != default_payday:
                # reset the curr_day to follow its original pay cycle
                curr_day = holiday

            if (holiday := (curr_day + frequency)) in holidays:
                curr_day = get_valid_payday(holiday)
            else:
                curr_day += frequency
        return False