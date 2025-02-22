from datetime import datetime, timedelta

def subtract_days_from_date(date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.
    
    Args:
        date (datetime or str): The input date to subtract days from. 
            If a string is provided, it should be in 'YYYY-MM-DD' format.
        days_to_subtract (int): Number of days to subtract from the date.
    
    Returns:
        datetime: A new date after subtracting the specified number of days.
    
    Raises:
        ValueError: If the input date is not a valid datetime or string,
                    or if days_to_subtract is not a non-negative integer.
    """
    # Validate input types
    if not isinstance(days_to_subtract, int):
        raise ValueError("days_to_subtract must be an integer")
    
    if days_to_subtract < 0:
        raise ValueError("days_to_subtract must be a non-negative integer")
    
    # Convert input to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date string. Use 'YYYY-MM-DD' format")
    
    # Validate input date type
    if not isinstance(date, datetime):
        raise ValueError("Input must be a datetime object or a date string")
    
    # Subtract days
    return date - timedelta(days=days_to_subtract)