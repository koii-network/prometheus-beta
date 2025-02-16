def is_leap_year(year):
    """
    Determine if a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4
    - But if it's also divisible by 100, it is NOT a leap year
    - Unless it is also divisible by 400, then it IS a leap year
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    
    Raises:
        TypeError: If the input is not an integer
        ValueError: If the input is not a positive year
    """
    # Check input type
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    
    # Check positive year
    if year <= 0:
        raise ValueError("Year must be a positive integer")
    
    # Leap year calculation logic
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)