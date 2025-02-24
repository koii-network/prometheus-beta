from datetime import datetime

def get_day_name(date_input):
    """
    Return the name of the day for a given date.

    Args:
        date_input (str or datetime): The date to get the day name for.
            Can be a string in format 'YYYY-MM-DD' or a datetime object.

    Returns:
        str: The name of the day (e.g., 'Monday', 'Tuesday', etc.)

    Raises:
        ValueError: If the input is not a valid date string or datetime object.
        TypeError: If the input is not a string or datetime object.
    """
    # Handle datetime input
    if isinstance(date_input, datetime):
        return date_input.strftime('%A')
    
    # Handle string input
    if isinstance(date_input, str):
        try:
            # Try parsing the date string
            parsed_date = datetime.strptime(date_input, '%Y-%m-%d')
            return parsed_date.strftime('%A')
        except ValueError:
            raise ValueError(f"Invalid date format. Use 'YYYY-MM-DD'. Got: {date_input}")
    
    # Raise TypeError for invalid input type
    raise TypeError(f"Expected str or datetime, got {type(date_input).__name__}")