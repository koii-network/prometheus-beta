from datetime import date, timedelta
from calendar import monthrange

def count_weekends_in_month(year: int, month: int) -> int:
    """
    Count the number of weekend days (Saturdays and Sundays) in a given month.
    
    Args:
        year (int): The year to check
        month (int): The month to check (1-12)
    
    Returns:
        int: Number of weekend days in the specified month
    
    Raises:
        ValueError: If month is not between 1 and 12
    """
    # Validate month input
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    # Get the number of days in the month and the day of the first day of the month
    _, num_days = monthrange(year, month)
    
    # Count weekends
    weekend_count = 0
    for day in range(1, num_days + 1):
        current_date = date(year, month, day)
        if current_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            weekend_count += 1
    
    return weekend_count