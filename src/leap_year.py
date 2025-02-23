def is_leap_year(year):
    """
    Determine if a given year is a leap year.
    
    A leap year is defined by the following rules:
    1. The year must be divisible by 4
    2. If the year is divisible by 100, it must also be divisible by 400 to be a leap year
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    
    Raises:
        TypeError: If the input is not an integer
        ValueError: If the input is not a positive integer
    """
    # Check if input is an integer
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    
    # Check if year is positive
    if year <= 0:
        raise ValueError("Year must be a positive integer")
    
    # Leap year rules:
    # 1. Divisible by 4
    # 2. If divisible by 100, must also be divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)