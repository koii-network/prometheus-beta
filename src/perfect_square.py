import math

def is_perfect_square(number):
    """
    Check if a given number is a perfect square.
    
    A perfect square is a number that can be expressed as the product of an integer with itself.
    
    Args:
        number (int or float): The number to check for being a perfect square.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    
    Raises:
        TypeError: If the input is not a number (int or float).
        ValueError: If the input is a negative number.
    
    Examples:
        >>> is_perfect_square(16)
        True
        >>> is_perfect_square(25)
        True
        >>> is_perfect_square(7)
        False
    """
    # Check input type
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    
    # Check for negative numbers
    if number < 0:
        raise ValueError("Input must be a non-negative number")
    
    # Special case for 0 and 1
    if number in (0, 1):
        return True
    
    # Calculate the square root and check if it's a whole number
    sqrt = math.sqrt(number)
    return math.isclose(sqrt, round(sqrt), rel_tol=1e-9)