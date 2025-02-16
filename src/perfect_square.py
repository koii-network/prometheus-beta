import math

def is_perfect_square(number):
    """
    Check if a given number is a perfect square.
    
    Args:
        number (int or float): The number to check.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    
    Raises:
        TypeError: If the input is not a number.
        ValueError: If the input is a negative number.
    """
    # Check input type
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    
    # Check for negative numbers
    if number < 0:
        raise ValueError("Input cannot be negative")
    
    # Special case for 0 and 1
    if number in (0, 1):
        return True
    
    # Calculate the square root
    root = math.isqrt(int(number))
    
    # Check if the square of the root equals the original number
    return root * root == number