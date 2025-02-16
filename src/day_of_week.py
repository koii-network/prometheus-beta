from datetime import datetime

def get_day_of_week(date_str):
    """
    Return the name of the day for a given date.
    
    Args:
        date_str (str): Date in format 'YYYY-MM-DD'
    
    Returns:
        str: Name of the day of the week
    
    Raises:
        ValueError: If the date is not in the correct format
    """
    try:
        # Parse the date string
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Return the day name (full name)
        return date_obj.strftime('%A')
    
    except ValueError:
        # Raise a descriptive error for invalid date format
        raise ValueError(f"Invalid date format. Please use 'YYYY-MM-DD'. Got: {date_str}")