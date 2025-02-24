import calendar
from datetime import date, timedelta

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

    # Get the number of days in the month
    cal = calendar.monthcalendar(year, month)
    
    # Count weekend days
    weekend_count = 0
    for week in cal:
        # Saturday is index 5, Sunday is index 6 in calendar.monthcalendar
        weekend_count += sum(1 for day in [week[5], week[6]] if day != 0)
    
    return weekend_count