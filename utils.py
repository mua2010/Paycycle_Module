from datetime import datetime

def get_valid_date_object(date: str) -> datetime.date:
    """Validates that the date passed in is in correct format: 'YYYY-MM-DD' and returns the date object."""
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise
    else:
        return date