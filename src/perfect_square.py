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
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0 and 1
    if number in [0, 1]:
        return True
    
    # Use integer square root method
    root = int(math.sqrt(number))
    return root * root == number