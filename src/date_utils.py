from datetime import datetime, timedelta

def add_days_to_date(date, days_to_add):
    """
    Add a specified number of days to a given date.
    
    Args:
        date (str or datetime): The input date in 'YYYY-MM-DD' format or datetime object
        days_to_add (int): Number of days to add to the date
    
    Returns:
        str: The resulting date in 'YYYY-MM-DD' format
    
    Raises:
        ValueError: If the input date is invalid or days_to_add is not an integer
    """
    # Convert input to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")
    
    # Validate days_to_add is an integer
    if not isinstance(days_to_add, int):
        raise ValueError("days_to_add must be an integer")
    
    # Add days and return as formatted string
    result_date = date + timedelta(days=days_to_add)
    return result_date.strftime('%Y-%m-%d')