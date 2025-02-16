from datetime import datetime, timedelta

def add_days_to_date(date_str: str, days: int) -> str:
    """
    Add n days to a given date string.
    
    Args:
        date_str (str): Date string in 'YYYY-MM-DD' format
        days (int): Number of days to add (can be positive or negative)
    
    Returns:
        str: Resulting date in 'YYYY-MM-DD' format
    
    Raises:
        ValueError: If date_str is not in the correct format
    """
    try:
        # Parse the input date string
        original_date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Add days using timedelta
        new_date = original_date + timedelta(days=days)
        
        # Return the new date as a formatted string
        return new_date.strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")