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
        TypeError: If the input date is not a datetime or string.
        ValueError: If the date cannot be parsed or days_to_subtract is negative.
    """
    # Handle string input
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    
    # Validate input
    if not isinstance(date, datetime):
        raise TypeError("Input must be a datetime object or a date string.")
    
    if not isinstance(days_to_subtract, int):
        raise TypeError("Days to subtract must be an integer.")
    
    if days_to_subtract < 0:
        raise ValueError("Days to subtract cannot be negative.")
    
    # Subtract days
    return date - timedelta(days=days_to_subtract)