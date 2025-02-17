import calendar
from datetime import date, timedelta

def count_weekends_in_month(year: int, month: int) -> int:
    """
    Count the number of weekend days (Saturdays and Sundays) in a given month.
    
    Args:
        year (int): The year to count weekends in
        month (int): The month to count weekends in (1-12)
    
    Returns:
        int: The total number of weekend days in the specified month
    
    Raises:
        ValueError: If the month is not between 1 and 12
    """
    # Validate month input
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    # Get the first and last day of the month
    first_day = date(year, month, 1)
    _, last_day_num = calendar.monthrange(year, month)
    last_day = date(year, month, last_day_num)
    
    # Count weekend days
    weekend_count = 0
    current_day = first_day
    
    while current_day <= last_day:
        if current_day.weekday() >= 5:  # 5 is Saturday, 6 is Sunday
            weekend_count += 1
        current_day += timedelta(days=1)
    
    return weekend_count