from datetime import datetime

def get_day_of_week(date_str):
    """
    Return the name of the day for a given date.

    Args:
        date_str (str): Date in the format 'YYYY-MM-DD'

    Returns:
        str: Name of the day (e.g., 'Monday', 'Tuesday', etc.)

    Raises:
        ValueError: If the date string is not in the correct format
    """
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Return the full name of the day
        return date_obj.strftime('%A')
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD' format.")