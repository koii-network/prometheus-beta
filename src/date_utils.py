from datetime import datetime

def calculate_days_between(date1, date2):
    """
    Calculate the number of days between two dates.
    
    Args:
        date1 (str or datetime): First date 
        date2 (str or datetime): Second date
    
    Returns:
        int: Number of days between the two dates (absolute value)
    
    Raises:
        ValueError: If dates cannot be parsed
    """
    # Convert input to datetime objects if they are strings
    if isinstance(date1, str):
        try:
            date1 = datetime.strptime(date1, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("First date must be in YYYY-MM-DD format")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.strptime(date2, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Second date must be in YYYY-MM-DD format")
    
    # Calculate absolute difference in days
    delta = abs((date2 - date1).days)
    
    return delta