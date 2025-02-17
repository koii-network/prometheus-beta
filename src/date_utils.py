from datetime import datetime, timedelta

def subtract_days_from_date(date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.

    Args:
        date (datetime or str): The input date to subtract days from.
                                If a string is provided, it should be in ISO format (YYYY-MM-DD).
        days_to_subtract (int): Number of days to subtract from the date.

    Returns:
        datetime: A new datetime object with the specified days subtracted.

    Raises:
        ValueError: If the input date is invalid or days_to_subtract is negative.
        TypeError: If the input types are incorrect.
    """
    # Validate input types
    if not isinstance(days_to_subtract, int):
        raise TypeError("days_to_subtract must be an integer")
    
    # Handle negative days
    if days_to_subtract < 0:
        raise ValueError("days_to_subtract must be a non-negative integer")
    
    # Convert input date to datetime object if it's a string
    if isinstance(date, str):
        try:
            date = datetime.fromisoformat(date)
        except ValueError:
            raise ValueError("Invalid date format. Use ISO format (YYYY-MM-DD)")
    
    # Validate datetime input
    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object or an ISO format string")
    
    # Subtract days
    return date - timedelta(days=days_to_subtract)