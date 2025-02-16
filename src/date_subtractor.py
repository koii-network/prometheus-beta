from datetime import datetime, timedelta

def subtract_days_from_date(date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.
    
    Args:
        date (datetime or str): The input date to subtract days from.
                                Can be a datetime object or a date string in ISO format (YYYY-MM-DD).
        days_to_subtract (int): Number of days to subtract from the input date.
    
    Returns:
        datetime: A new datetime object with the specified days subtracted.
    
    Raises:
        TypeError: If date is not a datetime or valid date string, or days_to_subtract is not an integer.
        ValueError: If the date string is not in the correct format.
    """
    # Validate input types
    if not isinstance(days_to_subtract, int):
        raise TypeError("days_to_subtract must be an integer")
    
    # Convert input to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.fromisoformat(date)
        except ValueError:
            raise ValueError("Date must be in ISO format (YYYY-MM-DD)")
    
    # Validate date type
    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object or ISO format date string")
    
    # Subtract days and return new datetime
    return date - timedelta(days=days_to_subtract)