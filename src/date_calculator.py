from datetime import datetime

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.
    
    Args:
        date1 (str): First date in the format 'YYYY-MM-DD'
        date2 (str): Second date in the format 'YYYY-MM-DD'
    
    Returns:
        int: Absolute number of days between the two dates
    
    Raises:
        ValueError: If dates are not in the correct format
    """
    try:
        # Parse the dates
        parsed_date1 = datetime.strptime(date1, '%Y-%m-%d')
        parsed_date2 = datetime.strptime(date2, '%Y-%m-%d')
        
        # Calculate the absolute number of days between dates
        delta = abs((parsed_date2 - parsed_date1).days)
        
        return delta
    except ValueError:
        raise ValueError("Dates must be in the format 'YYYY-MM-DD'")