import calendar
from datetime import date

def count_weekends_in_month(year: int, month: int) -> int:
    """
    Count the number of weekend days (Saturdays and Sundays) in a given month.
    
    Args:
        year (int): The year (e.g., 2023)
        month (int): The month (1-12)
    
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
    _, num_days = calendar.monthrange(year, month)
    
    # Count weekend days
    weekend_count = 0
    for day in range(1, num_days + 1):
        day_of_week = calendar.weekday(year, month, day)
        # 5 is Saturday, 6 is Sunday
        if day_of_week in [5, 6]:
            weekend_count += 1
    
    return weekend_count