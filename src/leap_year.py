def is_leap_year(year):
    """
    Determine if a given year is a leap year.
    
    A leap year is defined by the following rules:
    - Years divisible by 4 are leap years
    - However, years divisible by 100 are NOT leap years
    - Unless they are also divisible by 400, in which case they ARE leap years
    
    Args:
        year (int): The year to check for leap year status
    
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
    
    # Apply leap year rules
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)