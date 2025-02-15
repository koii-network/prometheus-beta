import calendar
from datetime import date, timedelta

def count_weekends_in_month(year: int, month: int) -> int:
    """
    Determine the number of weekend days (Saturdays and Sundays) in a given month.
    
    Args:
        year (int): The year (e.g., 2023)
        month (int): The month (1-12)
    
    Returns:
        int: Number of weekend days in the specified month
    
    Raises:
        ValueError: If the month is not between 1 and 12
    """
    # Validate month input
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    # Get the number of days in the month
    num_days = calendar.monthrange(year, month)[1]
    
    # Count weekend days
    weekend_count = 0
    for day in range(1, num_days + 1):
        current_date = date(year, month, day)
        if current_date.weekday() in [5, 6]:  # 5 is Saturday, 6 is Sunday
            weekend_count += 1
    
    return weekend_count