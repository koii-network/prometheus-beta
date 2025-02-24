def is_leap_year(year):
    """
    Determine if a given year is a leap year.
    
    A leap year is defined as:
    - A year divisible by 4
    - Except if it's divisible by 100, it must also be divisible by 400
    
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
    
    # Leap year conditions
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)