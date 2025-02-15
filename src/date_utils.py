from datetime import datetime, timedelta

def add_days_to_date(date_str: str, days: int) -> str:
    """
    Add n days to a given date string.
    
    Args:
        date_str (str): Input date string in format 'YYYY-MM-DD'
        days (int): Number of days to add (can be positive or negative)
    
    Returns:
        str: New date string in 'YYYY-MM-DD' format
    
    Raises:
        ValueError: If date_str is not in the correct format or days is not an integer
    """
    try:
        # Parse the input date string
        input_date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Add the specified number of days
        new_date = input_date + timedelta(days=days)
        
        # Return the new date as a formatted string
        return new_date.strftime('%Y-%m-%d')
    
    except ValueError as e:
        # Handle invalid date format or invalid days input
        raise ValueError(f"Invalid input: {e}. Ensure date is in 'YYYY-MM-DD' format and days is an integer.")