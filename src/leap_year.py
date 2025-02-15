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
        ValueError: If the input is not a positive integer
    """
    # Validate input
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")
    
    if year <= 0:
        raise ValueError("Year must be a positive integer")
    
    # Leap year calculation
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)