from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.

    Args:
        date (datetime or str): The starting date. 
            If str, must be in format 'YYYY-MM-DD'.
        days (int): Number of days to add. Can be positive or negative.

    Returns:
        datetime: The resulting date after adding specified days.

    Raises:
        ValueError: If the input date is invalid or days is not an integer.
        TypeError: If inputs are of incorrect type.
    """
    # Validate input types
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")

    # Convert string to datetime if needed
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format")
    
    # Validate datetime input
    if not isinstance(date, datetime):
        raise TypeError("Date must be a datetime object or a string")

    # Add days and return
    return date + timedelta(days=days)