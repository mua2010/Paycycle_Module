from datetime import datetime, date as date_class, timedelta

# Making sure that the next avaialble date is a business day AND nearest
def get_valid_payday(holiday: date_class) -> date_class:

    # for a weekday, monday is 0 and sunday is 6
    week_day_placeholder = (holiday + timedelta(days=1)).weekday()
    num_of_days_after = 1
    while week_day_placeholder in {5,6}:
        num_of_days_after += 1
        week_day_placeholder = (holiday + timedelta(days=num_of_days_after)).weekday()
        
    week_day_placeholder = (holiday - timedelta(days=1)).weekday()
    num_of_days_before = 1
    while week_day_placeholder in {5,6}:
        num_of_days_before += 1
        week_day_placeholder = (holiday - timedelta(days=num_of_days_before)).weekday()

    # POST PROCESS
    if num_of_days_before < num_of_days_after:
        return holiday - timedelta(days=num_of_days_before)
    else:
        return holiday + timedelta(days=num_of_days_after)
        
        
def get_valid_date_object(date: str) -> datetime.date:
    """Validates that the date passed in is in correct format: 'YYYY-MM-DD' and returns the date object."""
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise
    else:
        return date