from datetime import datetime, timedelta

def subtract_days_from_date(date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.
    
    Args:
        date (datetime or str): The input date to subtract days from.
        days_to_subtract (int): Number of days to subtract.
    
    Returns:
        datetime: A new date with the specified number of days subtracted.
    
    Raises:
        TypeError: If date is not a datetime object or valid date string.
        ValueError: If days_to_subtract is not a positive integer.
    """
    # Validate input types
    if not isinstance(days_to_subtract, int):
        raise TypeError("days_to_subtract must be an integer")
    
    if days_to_subtract < 0:
        raise ValueError("days_to_subtract must be a non-negative integer")
    
    # Handle different input date types
    if isinstance(date, str):
        try:
            date = datetime.fromisoformat(date)
        except ValueError:
            raise TypeError("date must be a datetime object or an ISO format date string")
    
    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object or an ISO format date string")
    
    # Subtract days
    return date - timedelta(days=days_to_subtract)