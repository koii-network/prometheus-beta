from datetime import datetime, timedelta

def subtract_days_from_date(date, days_to_subtract):
    """
    Subtract a specified number of days from a given date.

    Args:
        date (datetime or str): The input date to subtract days from.
                                Can be a datetime object or a date string in 'YYYY-MM-DD' format.
        days_to_subtract (int): Number of days to subtract from the date.

    Returns:
        datetime: A new datetime object with the specified number of days subtracted.

    Raises:
        TypeError: If date is not a datetime or str, or days_to_subtract is not an integer.
        ValueError: If date string is not in the correct format.
    """
    # Type checking
    if not isinstance(days_to_subtract, int):
        raise TypeError("days_to_subtract must be an integer")

    # Convert string to datetime if needed
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format")

    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object or a string in 'YYYY-MM-DD' format")

    # Subtract days
    return date - timedelta(days=days_to_subtract)