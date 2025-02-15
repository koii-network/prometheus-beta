from datetime import datetime

def get_day_name(date_input):
    """
    Return the name of the day for a given date.
    
    Args:
        date_input (str or datetime): Date to get the day name for
            - Accepts date string in format 'YYYY-MM-DD'
            - Accepts datetime object
    
    Returns:
        str: Name of the day (e.g., 'Monday', 'Tuesday', etc.)
    
    Raises:
        ValueError: If the input date is invalid or cannot be parsed
    """
    # If input is a string, convert to datetime
    if isinstance(date_input, str):
        try:
            date_obj = datetime.strptime(date_input, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'")
    
    # If input is already a datetime object
    elif isinstance(date_input, datetime):
        date_obj = date_input
    
    else:
        raise ValueError("Input must be a string in 'YYYY-MM-DD' format or a datetime object")
    
    # Return the day name
    return date_obj.strftime('%A')