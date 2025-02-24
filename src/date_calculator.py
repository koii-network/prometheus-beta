from datetime import datetime

def calculate_days_between_dates(date1: str, date2: str) -> int:
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str): First date in 'YYYY-MM-DD' format
        date2 (str): Second date in 'YYYY-MM-DD' format

    Returns:
        int: Absolute number of days between the two dates

    Raises:
        ValueError: If dates are not in the correct format or are invalid
    """
    try:
        # Parse dates using datetime
        parsed_date1 = datetime.strptime(date1, '%Y-%m-%d')
        parsed_date2 = datetime.strptime(date2, '%Y-%m-%d')

        # Calculate the absolute difference in days
        delta = abs((parsed_date2 - parsed_date1).days)

        return delta
    except ValueError as e:
        # Catch and re-raise with a more informative message
        raise ValueError(f"Invalid date format. Dates must be in 'YYYY-MM-DD' format: {e}")