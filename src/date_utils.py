from datetime import datetime

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.
    
    Args:
        date1 (str or datetime): First date in 'YYYY-MM-DD' format or datetime object
        date2 (str or datetime): Second date in 'YYYY-MM-DD' format or datetime object
    
    Returns:
        int: Number of days between the two dates (absolute value)
    
    Raises:
        ValueError: If dates are in invalid format
    """
    # Convert string inputs to datetime objects if needed
    if isinstance(date1, str):
        try:
            date1 = datetime.strptime(date1, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("First date must be in 'YYYY-MM-DD' format")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.strptime(date2, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Second date must be in 'YYYY-MM-DD' format")
    
    # Calculate absolute difference in days
    return abs((date2 - date1).days)