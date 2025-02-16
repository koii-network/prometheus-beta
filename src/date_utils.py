from datetime import datetime, timedelta

def add_days_to_date(date_str: str, days: int) -> str:
    """
    Add a specified number of days to a given date.
    
    Args:
        date_str (str): Date in the format 'YYYY-MM-DD'
        days (int): Number of days to add (can be positive or negative)
    
    Returns:
        str: Resulting date in the format 'YYYY-MM-DD'
    
    Raises:
        ValueError: If the input date string is not in the correct format
    """
    try:
        # Parse the input date string 
        original_date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Add the specified number of days
        new_date = original_date + timedelta(days=days)
        
        # Return the new date as a formatted string
        return new_date.strftime('%Y-%m-%d')
    except ValueError as e:
        raise ValueError(f"Invalid date format. Please use 'YYYY-MM-DD': {e}")