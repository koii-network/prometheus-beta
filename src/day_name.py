from datetime import datetime, date

def get_day_name(input_date):
    """
    Return the name of the day for a given date.

    Args:
        input_date (date or str): The date to get the day name for. 
                                  Can be a datetime.date object or a string 
                                  in 'YYYY-MM-DD' format.

    Returns:
        str: The name of the day (e.g., 'Monday', 'Tuesday', etc.)

    Raises:
        ValueError: If the input date is not in a valid format or cannot be parsed.
    """
    # If input is a string, convert to date object
    if isinstance(input_date, str):
        try:
            input_date = datetime.strptime(input_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    
    # Validate input is a date object
    if not isinstance(input_date, date):
        raise ValueError("Input must be a date object or a string in 'YYYY-MM-DD' format.")
    
    # Get day name (first letter capitalized)
    return input_date.strftime('%A')