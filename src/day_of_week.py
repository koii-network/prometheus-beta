from datetime import datetime

def get_day_of_week(date_input):
    """
    Return the name of the day for a given date.
    
    Args:
        date_input (str or datetime): The date to get the day name for.
                                      Accepts date strings in format 'YYYY-MM-DD' 
                                      or datetime objects.
    
    Returns:
        str: Name of the day (e.g., 'Monday', 'Tuesday', etc.)
    
    Raises:
        ValueError: If the input is not a valid date
    """
    # If input is a string, convert to datetime
    if isinstance(date_input, str):
        try:
            date_input = datetime.strptime(date_input, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
    
    # If input is not a datetime object, raise an error
    if not isinstance(date_input, datetime):
        raise ValueError("Input must be a date string or datetime object.")
    
    # Return the day name
    return date_input.strftime('%A')