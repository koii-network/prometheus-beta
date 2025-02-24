from datetime import datetime, timedelta

def subtract_days(date, days):
    """
    Subtract a specified number of days from a given date.

    Args:
        date (datetime or str): The input date to subtract days from. 
            If a string is provided, it should be in ISO format (YYYY-MM-DD).
        days (int): Number of days to subtract. Must be a non-negative integer.

    Returns:
        datetime: A new datetime object representing the date after subtraction.

    Raises:
        ValueError: If days is negative or input date is invalid.
        TypeError: If input types are incorrect.
    """
    # Validate input types
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")
    
    # Ensure days is non-negative
    if days < 0:
        raise ValueError("Number of days to subtract must be non-negative")

    # Convert input to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.fromisoformat(date)
        except ValueError:
            raise ValueError("Invalid date format. Use ISO format (YYYY-MM-DD)")
    
    # Validate input date type
    if not isinstance(date, datetime):
        raise TypeError("Date must be a datetime object or ISO format string")

    # Subtract days and return new date
    return date - timedelta(days=days)