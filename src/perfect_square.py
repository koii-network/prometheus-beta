import math

def is_perfect_square(n):
    """
    Check if a given number is a perfect square.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0 and 1
    if n == 0 or n == 1:
        return True
    
    # Find the square root
    root = int(math.sqrt(n))
    
    # Check if the square of the root equals the original number
    return root * root == n