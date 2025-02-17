from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.
    
    Args:
        date (str or datetime): The input date in 'YYYY-MM-DD' format or a datetime object
        days (int): Number of days to add (can be positive or negative)
    
    Returns:
        str: Resulting date in 'YYYY-MM-DD' format
    
    Raises:
        ValueError: If the input date is not in a valid format
        TypeError: If days is not an integer
    """
    # Validate input type for days
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")
    
    # Convert input to datetime object if it's a string
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")
    
    # Add days
    new_date = date + timedelta(days=days)
    
    # Return formatted date string
    return new_date.strftime('%Y-%m-%d')