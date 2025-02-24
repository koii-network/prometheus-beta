import math

def is_perfect_square(n: int) -> bool:
    """
    Check if a given number is a perfect square.

    A perfect square is an integer that is the square of another integer.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    
    Examples:
        >>> is_perfect_square(16)
        True
        >>> is_perfect_square(14)
        False
        >>> is_perfect_square(0)
        True
    """
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check for negative numbers
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases
    if n == 0 or n == 1:
        return True
    
    # Use integer square root method
    # A number is a perfect square if its square root is an integer
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n