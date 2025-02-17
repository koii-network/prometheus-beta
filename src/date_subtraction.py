from datetime import datetime, timedelta

def subtract_days_from_date(input_date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.
    
    Args:
        input_date (datetime or str): The date to subtract days from.
                                      If str, should be in format 'YYYY-MM-DD'.
        days_to_subtract (int): Number of days to subtract.
    
    Returns:
        datetime: The resulting date after subtraction.
    
    Raises:
        ValueError: If input_date is not a valid datetime or str,
                    or if days_to_subtract is not a non-negative integer.
    """
    # Validate input type
    if not isinstance(days_to_subtract, int):
        raise ValueError("days_to_subtract must be an integer")
    
    if days_to_subtract < 0:
        raise ValueError("days_to_subtract must be a non-negative integer")
    
    # Convert input_date to datetime if it's a string
    if isinstance(input_date, str):
        try:
            input_date = datetime.strptime(input_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("input_date string must be in format 'YYYY-MM-DD'")
    
    # Validate input_date is a datetime
    if not isinstance(input_date, datetime):
        raise ValueError("input_date must be a datetime or a string in 'YYYY-MM-DD' format")
    
    # Subtract days
    return input_date - timedelta(days=days_to_subtract)