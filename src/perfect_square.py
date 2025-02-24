import math

def is_perfect_square(number: int) -> bool:
    """
    Check if a given number is a perfect square.

    A perfect square is an integer that is the square of another integer.

    Args:
        number (int): The number to check for being a perfect square.

    Returns:
        bool: True if the number is a perfect square, False otherwise.

    Raises:
        ValueError: If the input is a negative number.

    Examples:
        >>> is_perfect_square(16)
        True
        >>> is_perfect_square(25)
        True
        >>> is_perfect_square(7)
        False
        >>> is_perfect_square(0)
        True
    """
    # Check for negative numbers
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle special cases
    if number == 0 or number == 1:
        return True
    
    # Calculate the square root and check if it's an integer
    root = int(math.sqrt(number))
    return root * root == number