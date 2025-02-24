from datetime import datetime, timedelta

def subtract_days(date: datetime, days: int) -> datetime:
    """
    Subtract a specified number of days from a given date.

    Args:
        date (datetime): The original date
        days (int): Number of days to subtract (must be non-negative)

    Returns:
        datetime: A new datetime object with the specified number of days subtracted

    Raises:
        ValueError: If days is negative
    """
    if days < 0:
        raise ValueError("Number of days to subtract must be non-negative")
    
    return date - timedelta(days=days)