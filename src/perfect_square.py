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
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # If number is 0 or 1, it's a perfect square
    if number in [0, 1]:
        return True
    
    # Use integer square root and check if squaring it gives the original number
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number