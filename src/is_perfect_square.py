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
    # Validate input
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0 and 1
    if number in (0, 1):
        return True
    
    # Calculate the square root
    root = int(math.sqrt(number))
    
    # Check if the square of the root equals the original number
    return root * root == number