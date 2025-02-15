from datetime import datetime, timedelta

def subtract_days_from_date(date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.
    
    Args:
        date (datetime or str): The input date to subtract days from. 
                                If a string, it should be in 'YYYY-MM-DD' format.
        days_to_subtract (int): Number of days to subtract from the date.
    
    Returns:
        datetime: A new date with the specified number of days subtracted.
    
    Raises:
        ValueError: If the input is not a valid date or days_to_subtract is negative.
    """
    # Validate input type and convert if necessary
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
    
    # Validate days_to_subtract
    if not isinstance(days_to_subtract, int):
        raise ValueError("days_to_subtract must be an integer")
    
    if days_to_subtract < 0:
        raise ValueError("days_to_subtract cannot be negative")
    
    # Subtract days
    return date - timedelta(days=days_to_subtract)