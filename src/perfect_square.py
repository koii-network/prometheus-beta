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
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check for negative numbers
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0 and 1
    if n in [0, 1]:
        return True
    
    # Calculate the square root and check if it's a whole number
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n