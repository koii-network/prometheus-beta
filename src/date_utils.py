from datetime import datetime, timedelta

def add_days_to_date(input_date, days_to_add):
    """
    Add a specified number of days to a given date.
    
    Args:
        input_date (str or datetime): The input date to modify.
        days_to_add (int): Number of days to add to the input date.
    
    Returns:
        datetime: A new datetime object representing the date after adding days.
    
    Raises:
        ValueError: If input_date is not a valid date or days_to_add is not an integer.
    """
    # Convert input to datetime if it's a string
    if isinstance(input_date, str):
        try:
            input_date = datetime.strptime(input_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    
    # Validate input types
    if not isinstance(input_date, datetime):
        raise ValueError("Input must be a datetime object or a date string.")
    
    if not isinstance(days_to_add, int):
        raise ValueError("Number of days must be an integer.")
    
    # Add days and return the new date
    return input_date + timedelta(days=days_to_add)