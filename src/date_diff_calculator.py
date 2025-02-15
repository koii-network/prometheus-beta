from datetime import datetime

def calculate_days_between_dates(date1, date2):
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
        parsed_date1 = datetime.strptime(date1, "%Y-%m-%d")
        parsed_date2 = datetime.strptime(date2, "%Y-%m-%d")
        
        # Calculate the absolute difference in days
        days_difference = abs((parsed_date2 - parsed_date1).days)
        
        return days_difference
    
    except ValueError as e:
        raise ValueError(f"Invalid date format. Use 'YYYY-MM-DD'. Error: {e}")