import math

def is_perfect_square(num):
    """
    Check if a given number is a perfect square.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Check if input is an integer
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if num < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0 and 1
    if num in [0, 1]:
        return True
    
    # Use integer square root to check
    root = int(math.sqrt(num))
    return root * root == num