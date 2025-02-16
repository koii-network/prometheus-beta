def is_leap_year(year):
    """
    Determine if a given year is a leap year.
    
    A leap year is defined as:
    - A year divisible by 4
    - Except years divisible by 100 are not leap years
    - Unless they are also divisible by 400, then they are leap years
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    
    Raises:
        TypeError: If the input is not an integer
        ValueError: If the year is not a positive integer
    """
    # Check input type
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    
    # Check year is positive
    if year <= 0:
        raise ValueError("Year must be a positive integer")
    
    # Leap year calculation
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)