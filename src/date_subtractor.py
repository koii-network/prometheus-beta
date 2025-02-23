from datetime import datetime, timedelta

def subtract_days_from_date(date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.

    Args:
        date (datetime or str): The input date to subtract days from.
            If a string is provided, it should be in ISO format (YYYY-MM-DD).
        days_to_subtract (int): Number of days to subtract from the date.

    Returns:
        datetime: A new datetime object with the specified number of days subtracted.

    Raises:
        TypeError: If the input date is not a datetime or valid date string.
        ValueError: If days_to_subtract is not a non-negative integer.
    """
    # Validate input date
    if isinstance(date, str):
        try:
            date = datetime.fromisoformat(date)
        except ValueError:
            raise TypeError("Date must be a datetime object or a string in ISO format (YYYY-MM-DD)")
    
    if not isinstance(date, datetime):
        raise TypeError("Date must be a datetime object or a string in ISO format (YYYY-MM-DD)")
    
    # Validate days_to_subtract
    if not isinstance(days_to_subtract, int):
        raise TypeError("Days to subtract must be an integer")
    
    if days_to_subtract < 0:
        raise ValueError("Days to subtract must be a non-negative integer")
    
    # Subtract days
    return date - timedelta(days=days_to_subtract)