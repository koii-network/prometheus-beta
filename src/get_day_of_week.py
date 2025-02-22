from datetime import datetime

def get_day_of_week(date_string):
    """
    Return the name of the day for a given date.
    
    Args:
        date_string (str): Date in format 'YYYY-MM-DD'
    
    Returns:
        str: Name of the day of the week
    
    Raises:
        ValueError: If the date string is not in the correct format
    """
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        
        # Get the day name (full name)
        day_name = date_obj.strftime('%A')
        
        return day_name
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")