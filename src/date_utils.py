from datetime import datetime, timedelta

def add_days_to_date(input_date, days_to_add):
    """
    Add a specified number of days to a given date.

    Args:
        input_date (datetime or str): The starting date to add days to.
            If a string is provided, it should be in ISO format (YYYY-MM-DD).
        days_to_add (int): Number of days to add to the input date.

    Returns:
        date: A new date object representing the date after adding days.

    Raises:
        TypeError: If input_date is not a datetime or valid date string.
        ValueError: If days_to_add is not an integer.
    """
    # Validate input date
    if isinstance(input_date, str):
        try:
            input_date = datetime.fromisoformat(input_date).date()
        except ValueError:
            raise TypeError("Input date must be a datetime object or a string in ISO format (YYYY-MM-DD)")
    elif isinstance(input_date, datetime):
        input_date = input_date.date()
    
    # Validate days_to_add
    if not isinstance(days_to_add, int):
        raise ValueError("Number of days must be an integer")

    # Add days and return
    return input_date + timedelta(days=days_to_add)