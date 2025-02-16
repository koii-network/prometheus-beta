def is_leap_year(year):
    """
    Determine if a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4
    - BUT if it's divisible by 100, it is NOT a leap year
    - UNLESS it is also divisible by 400, then it IS a leap year
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    
    Raises:
        TypeError: If the input is not an integer
        ValueError: If the input year is not a positive integer
    """
    # Check if input is an integer
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    
    # Check if year is a positive integer
    if year <= 0:
        raise ValueError("Year must be a positive integer")
    
    # Leap year rules
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)