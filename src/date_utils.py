from datetime import datetime, timedelta

def add_days_to_date(date_str: str, days: int) -> str:
    """
    Add a specified number of days to a given date.
    
    Args:
        date_str (str): Input date in 'YYYY-MM-DD' format
        days (int): Number of days to add (can be positive or negative)
    
    Returns:
        str: Resulting date in 'YYYY-MM-DD' format
    
    Raises:
        ValueError: If date_str is not in the correct format
    """
    try:
        # Parse the input date string
        input_date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Add the specified number of days
        new_date = input_date + timedelta(days=days)
        
        # Return the new date as a formatted string
        return new_date.strftime('%Y-%m-%d')
    except ValueError as e:
        # Handle incorrect date format
        raise ValueError(f"Invalid date format. Please use 'YYYY-MM-DD'. Error: {str(e)}")