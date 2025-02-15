from datetime import datetime, timedelta

def add_days_to_date(input_date, days_to_add):
    """
    Add a specified number of days to a given date.
    
    Args:
        input_date (str or datetime): The input date to add days to.
                                      Accepts date string in format 'YYYY-MM-DD' or datetime object.
        days_to_add (int): Number of days to add to the input date.
    
    Returns:
        datetime: A new datetime object representing the date after adding the specified days.
    
    Raises:
        ValueError: If input_date is not a valid date string or datetime object,
                    or if days_to_add is not an integer.
    """
    # Validate input_date type
    if isinstance(input_date, str):
        try:
            input_date = datetime.strptime(input_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Input date must be in 'YYYY-MM-DD' format")
    
    # Validate input_date is a datetime object
    if not isinstance(input_date, datetime):
        raise ValueError("Input must be a datetime object or a date string")
    
    # Validate days_to_add is an integer
    if not isinstance(days_to_add, int):
        raise ValueError("Days to add must be an integer")
    
    # Add days and return the new date
    return input_date + timedelta(days=days_to_add)