from datetime import datetime

def calculate_days_between_dates(date1: str, date2: str) -> int:
    """
    Calculate the number of days between two dates.
    
    Args:
        date1 (str): First date in 'YYYY-MM-DD' format
        date2 (str): Second date in 'YYYY-MM-DD' format
    
    Returns:
        int: Absolute number of days between the two dates
    
    Raises:
        ValueError: If dates are not in the correct format
    """
    try:
        # Parse dates from string to datetime objects
        first_date = datetime.strptime(date1, '%Y-%m-%d')
        second_date = datetime.strptime(date2, '%Y-%m-%d')
        
        # Calculate the absolute difference in days
        delta = abs((second_date - first_date).days)
        
        return delta
    except ValueError:
        raise ValueError("Dates must be in 'YYYY-MM-DD' format")