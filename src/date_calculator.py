from datetime import datetime

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.
    
    Args:
        date1 (str or datetime): First date 
        date2 (str or datetime): Second date
    
    Returns:
        int: Absolute number of days between the two dates
    
    Raises:
        ValueError: If dates cannot be parsed
    """
    # Convert inputs to datetime if they are strings
    if isinstance(date1, str):
        try:
            date1 = datetime.fromisoformat(date1.replace('Z', '+00:00'))
        except ValueError:
            try:
                date1 = datetime.strptime(date1, '%Y-%m-%d')
            except ValueError:
                raise ValueError(f"Unable to parse first date: {date1}")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.fromisoformat(date2.replace('Z', '+00:00'))
        except ValueError:
            try:
                date2 = datetime.strptime(date2, '%Y-%m-%d')
            except ValueError:
                raise ValueError(f"Unable to parse second date: {date2}")
    
    # Calculate the absolute difference in days
    delta = abs((date2 - date1).days)
    
    return delta