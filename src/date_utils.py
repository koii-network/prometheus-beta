from datetime import datetime

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str or datetime): The first date 
        date2 (str or datetime): The second date

    Returns:
        int: The absolute number of days between the two dates

    Raises:
        ValueError: If the input dates are invalid or cannot be parsed
        TypeError: If input is not a string or datetime object
    """
    # Convert input to datetime objects if they are strings
    if isinstance(date1, str):
        try:
            date1 = datetime.fromisoformat(date1)
        except ValueError:
            try:
                date1 = datetime.strptime(date1, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"Unable to parse date1: {date1}")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.fromisoformat(date2)
        except ValueError:
            try:
                date2 = datetime.strptime(date2, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"Unable to parse date2: {date2}")
    
    # Validate input types
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise TypeError("Input must be datetime objects or date strings")
    
    # Calculate the absolute number of days between dates
    delta = abs((date2 - date1).days)
    
    return delta