from datetime import datetime, date

def get_day_name(input_date):
    """
    Return the name of the day for a given date.

    Args:
        input_date (date or str): The date to get the day name for. 
                                  Can be a datetime.date object or 
                                  a string in 'YYYY-MM-DD' format.

    Returns:
        str: The full name of the day (e.g., 'Monday', 'Tuesday', etc.)

    Raises:
        ValueError: If the input is not a valid date or cannot be parsed.
        TypeError: If the input is not a date or string.
    """
    # Convert string input to date object if needed
    if isinstance(input_date, str):
        try:
            input_date = datetime.strptime(input_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError(f"Invalid date string. Use format 'YYYY-MM-DD'. Got: {input_date}")
    
    # Validate input is a date object
    if not isinstance(input_date, date):
        raise TypeError(f"Input must be a date object or string. Got: {type(input_date)}")
    
    # Return the day name
    return input_date.strftime('%A')