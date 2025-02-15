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
    # Check if the input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check if the input is non-negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # If number is 0 or 1, it's a perfect square
    if number in (0, 1):
        return True
    
    # Find the integer square root
    sqrt = int(math.sqrt(number))
    
    # Check if the square of the root equals the original number
    return sqrt * sqrt == number