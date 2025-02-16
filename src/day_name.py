from datetime import datetime

def get_day_name(date):
    """
    Return the name of the day for a given date.
    
    Args:
        date (str or datetime): A date in string format (YYYY-MM-DD) or datetime object
    
    Returns:
        str: Name of the day (e.g., 'Monday', 'Tuesday', etc.)
    
    Raises:
        ValueError: If the input date is not in a valid format
    """
    # If input is a string, convert to datetime
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
    
    # If input is not a datetime object, raise an error
    if not isinstance(date, datetime):
        raise TypeError("Input must be a string in YYYY-MM-DD format or a datetime object")
    
    # Return the day name
    return date.strftime('%A')