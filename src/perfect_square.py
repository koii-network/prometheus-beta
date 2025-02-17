import math

def is_perfect_square(number):
    """
    Check if a given number is a perfect square.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Check input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check if number is negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Check if number is zero or one (special perfect squares)
    if number in [0, 1]:
        return True
    
    # Calculate square root and check if it's a whole number
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number