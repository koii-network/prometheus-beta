from datetime import datetime

def get_day_name(date):
    """
    Return the name of the day for a given date.
    
    Args:
        date (str or datetime): Date to get the day name for. 
                                Accepts date strings in 'YYYY-MM-DD' format 
                                or datetime objects.
    
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
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'")
    
    # If input is not a datetime object, raise error
    if not isinstance(date, datetime):
        raise TypeError("Input must be a date string or datetime object")
    
    # Return the day name
    return date.strftime('%A')