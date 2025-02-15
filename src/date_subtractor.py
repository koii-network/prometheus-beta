from datetime import datetime, timedelta

def subtract_days_from_date(date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.
    
    Args:
        date (datetime or str): The input date to subtract days from.
                                Can be a datetime object or a date string.
        days_to_subtract (int): Number of days to subtract from the date.
    
    Returns:
        datetime: A new datetime object with days subtracted.
    
    Raises:
        ValueError: If the input is not a valid datetime or days_to_subtract is negative.
        TypeError: If the input types are incorrect.
    """
    # Validate input types
    if not isinstance(days_to_subtract, int):
        raise TypeError("days_to_subtract must be an integer")
    
    if days_to_subtract < 0:
        raise ValueError("days_to_subtract must be a non-negative integer")
    
    # Convert input to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.fromisoformat(date)
        except ValueError:
            raise ValueError("Invalid date string format. Use ISO format (YYYY-MM-DD)")
    
    # Validate datetime input
    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object or an ISO formatted date string")
    
    return date - timedelta(days=days_to_subtract)