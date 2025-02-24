import calendar
from datetime import date

def count_weekends_in_month(year: int, month: int) -> int:
    """
    Count the number of weekend days (Saturdays and Sundays) in a given month.

    Args:
        year (int): The year to check (4-digit year)
        month (int): The month to check (1-12)

    Returns:
        int: Number of weekend days in the specified month

    Raises:
        ValueError: If year or month is invalid
    """
    # Validate input
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    if year < 1:
        raise ValueError("Year must be a positive integer")

    # Get the first and last day of the month
    _, last_day_num = calendar.monthrange(year, month)

    # Count weekend days by iterating through each day
    weekend_count = sum(
        1 for day in range(1, last_day_num + 1)
        if date(year, month, day).weekday() >= 5  # 5 = Saturday, 6 = Sunday
    )
    
    return weekend_count