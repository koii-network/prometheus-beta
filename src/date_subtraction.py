from datetime import datetime, timedelta

def subtract_days_from_date(date: datetime, days: int) -> datetime:
    """
    Subtract a specified number of days from a given date.

    Args:
        date (datetime): The original date
        days (int): Number of days to subtract

    Returns:
        datetime: A new datetime object with the specified number of days subtracted

    Raises:
        TypeError: If date is not a datetime object or days is not an integer
        ValueError: If days is negative
    """
    if not isinstance(date, datetime):
        raise TypeError("Input date must be a datetime object")
    
    if not isinstance(days, int):
        raise TypeError("Number of days must be an integer")
    
    if days < 0:
        raise ValueError("Number of days cannot be negative")
    
    return date - timedelta(days=days)