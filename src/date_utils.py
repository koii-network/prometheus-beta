from datetime import datetime, timedelta

def add_days_to_date(input_date, days_to_add):
    """
    Add a specified number of days to a given date.
    
    Args:
        input_date (str or datetime): The input date to add days to.
                                      Can be a string in 'YYYY-MM-DD' format 
                                      or a datetime object.
        days_to_add (int): Number of days to add to the input date.
    
    Returns:
        datetime: A new datetime object with days added.
    
    Raises:
        ValueError: If input_date is not a valid date or days_to_add is not an integer.
    """
    # Validate input type
    if not isinstance(days_to_add, int):
        raise ValueError("days_to_add must be an integer")
    
    # Convert input to datetime if it's a string
    if isinstance(input_date, str):
        try:
            input_date = datetime.strptime(input_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("input_date must be in 'YYYY-MM-DD' format")
    
    # Validate input_date is a datetime object
    if not isinstance(input_date, datetime):
        raise ValueError("input_date must be a datetime object or a string in 'YYYY-MM-DD' format")
    
    # Add days and return
    return input_date + timedelta(days=days_to_add)