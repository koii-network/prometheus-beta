from datetime import datetime, timedelta

def subtract_days_from_date(input_date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.
    
    Args:
        input_date (datetime or str): The date to subtract days from. 
            If a string is provided, it should be in 'YYYY-MM-DD' format.
        days_to_subtract (int): Number of days to subtract from the input date.
    
    Returns:
        datetime: A new date after subtracting the specified number of days.
    
    Raises:
        ValueError: If input_date is not a valid datetime or string,
                    or if days_to_subtract is not a non-negative integer.
    """
    # Validate input date
    if isinstance(input_date, str):
        try:
            input_date = datetime.strptime(input_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Input date must be in 'YYYY-MM-DD' format")
    
    # Validate input date type
    if not isinstance(input_date, datetime):
        raise ValueError("Input date must be a datetime object or a string")
    
    # Validate days_to_subtract
    if not isinstance(days_to_subtract, int):
        raise ValueError("Days to subtract must be an integer")
    
    if days_to_subtract < 0:
        raise ValueError("Days to subtract must be a non-negative integer")
    
    # Subtract days
    return input_date - timedelta(days=days_to_subtract)