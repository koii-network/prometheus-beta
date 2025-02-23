from datetime import date, timedelta

def count_weekends_in_month(year: int, month: int) -> int:
    """
    Count the number of weekend days (Saturdays and Sundays) in a given month.

    Args:
        year (int): The year of the month to count weekends in.
        month (int): The month to count weekends in (1-12).

    Returns:
        int: Number of weekend days in the specified month.

    Raises:
        ValueError: If the month is not between 1 and 12.
    """
    # Validate month input
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12")

    # Create dates for the first and last day of the month
    first_day = date(year, month, 1)
    
    # Determine the last day of the month
    if month == 12:
        last_day = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = date(year, month + 1, 1) - timedelta(days=1)

    # Count weekends
    weekend_count = 0
    current_date = first_day
    while current_date <= last_day:
        # Check if current day is a weekend (Saturday or Sunday)
        if current_date.weekday() in [5, 6]:  # 5 is Saturday, 6 is Sunday
            weekend_count += 1
        current_date += timedelta(days=1)

    return weekend_count