from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.

    Args:
        date (str or datetime): The input date to add days to.
            Can be a datetime object or a string in 'YYYY-MM-DD' format.
        days (int): Number of days to add to the date.
            Can be positive (to add days) or negative (to subtract days).

    Returns:
        datetime: A new datetime object representing the date after adding days.

    Raises:
        ValueError: If the input date is not in a valid format or days is not an integer.
        TypeError: If the input date is not a string or datetime object.
    """
    # Validate input types
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")

    # Convert input to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")
    elif not isinstance(date, datetime):
        raise TypeError("Date must be a string in 'YYYY-MM-DD' format or a datetime object")

    # Add days and return the new date
    return date + timedelta(days=days)