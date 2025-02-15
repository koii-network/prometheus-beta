from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.
    
    Args:
        date (str or datetime): The input date to add days to.
                                Accepts date string in 'YYYY-MM-DD' format or datetime object.
        days (int): Number of days to add (can be positive or negative).
    
    Returns:
        datetime: A new datetime object representing the date after adding the specified days.
    
    Raises:
        ValueError: If the input date is not in the correct format or is invalid.
        TypeError: If days is not an integer.
    """
    # Validate input types
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")
    
    # Handle string input
    if isinstance(date, str):
        try:
            # Parse the date string
            parsed_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")
    
    # Handle datetime input
    elif isinstance(date, datetime):
        parsed_date = date
    
    else:
        raise TypeError("Date must be a string ('YYYY-MM-DD') or datetime object")
    
    # Add days
    return parsed_date + timedelta(days=days)