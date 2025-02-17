from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.
    
    Args:
        date (str or datetime): The input date to add days to.
                                Supports string format 'YYYY-MM-DD' or datetime object.
        days (int): Number of days to add. Can be positive or negative.
    
    Returns:
        datetime: A new datetime object with days added.
    
    Raises:
        ValueError: If the input date is not in a valid format.
        TypeError: If days is not an integer.
    """
    # Validate input types
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")
    
    # Convert string to datetime if needed
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format")
    
    # Validate datetime input
    if not isinstance(date, datetime):
        raise TypeError("Date must be a string in 'YYYY-MM-DD' format or a datetime object")
    
    # Add days and return new datetime
    return date + timedelta(days=days)