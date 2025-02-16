from datetime import datetime, timedelta

def add_days_to_date(date, n_days):
    """
    Add a specified number of days to a given date.
    
    Args:
        date (str or datetime): The input date 
            - If str: expects format 'YYYY-MM-DD'
            - If datetime: accepts datetime object
        n_days (int): Number of days to add (can be positive or negative)
    
    Returns:
        datetime: A new datetime object representing the date after adding days
    
    Raises:
        ValueError: If the input date is in an invalid format or n_days is not an integer
    """
    # Validate input type for date
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format")
    
    # Validate input type for n_days
    if not isinstance(n_days, int):
        raise ValueError("Number of days must be an integer")
    
    # Add days and return the new date
    return date + timedelta(days=n_days)