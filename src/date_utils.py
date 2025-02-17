from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.
    
    Args:
        date (datetime or str): The starting date. 
                                If a string, should be in 'YYYY-MM-DD' format.
        days (int): Number of days to add (can be positive or negative)
    
    Returns:
        datetime: A new date after adding the specified number of days
    
    Raises:
        ValueError: If the input date is invalid or days is not an integer
    """
    # Validate input type for days
    if not isinstance(days, int):
        raise ValueError("Days must be an integer")
    
    # Convert string input to datetime if needed
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format")
    
    # Validate input type for date
    if not isinstance(date, datetime):
        raise ValueError("Date must be a datetime object or a string")
    
    # Add days and return new date
    return date + timedelta(days=days)