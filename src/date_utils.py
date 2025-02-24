from datetime import datetime, date

def get_day_name(input_date):
    """
    Return the name of the day for a given date.

    Args:
        input_date (date or str): The date to get the day name for. 
                                  Can be a datetime.date object or a date string in YYYY-MM-DD format.

    Returns:
        str: The name of the day (e.g., 'Monday', 'Tuesday', etc.)

    Raises:
        ValueError: If the input is not a valid date or date string
        TypeError: If the input is not a date or string
    """
    # Handle different input types
    if isinstance(input_date, str):
        try:
            # Try to parse the string into a date object
            input_date = datetime.strptime(input_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date string. Use YYYY-MM-DD format.")
    
    # Ensure input is a date object
    if not isinstance(input_date, date):
        raise TypeError("Input must be a date object or a date string in YYYY-MM-DD format")
    
    # Return the day name
    return input_date.strftime('%A')