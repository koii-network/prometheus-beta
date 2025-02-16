from datetime import datetime, timedelta

def subtract_days_from_date(date, days):
    """
    Subtract a specified number of days from a given date.
    
    Args:
        date (datetime or str): The original date. Can be a datetime object or a string.
        days (int): Number of days to subtract.
    
    Returns:
        datetime: A new datetime object with the specified number of days subtracted.
    
    Raises:
        TypeError: If date is not a datetime or valid date string, or days is not an integer.
        ValueError: If the date string cannot be parsed.
    """
    # Check input types
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")
    
    # Convert input date to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date string must be in format 'YYYY-MM-DD'")
    
    # Check if date is a datetime object
    if not isinstance(date, datetime):
        raise TypeError("Date must be a datetime object or a string in 'YYYY-MM-DD' format")
    
    # Subtract days
    return date - timedelta(days=days)