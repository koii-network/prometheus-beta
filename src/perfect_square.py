import math

def is_perfect_square(number):
    """
    Check if a given number is a perfect square.

    A perfect square is a number that can be expressed as the product of an integer with itself.

    Args:
        number (int or float): The number to check for being a perfect square.

    Returns:
        bool: True if the number is a perfect square, False otherwise.

    Raises:
        TypeError: If the input is not a numeric type.
        ValueError: If the input is a negative number.
    """
    # Check input type
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a numeric type")

    # Check for negative numbers
    if number < 0:
        raise ValueError("Input must be a non-negative number")

    # Handle zero and one as special cases
    if number in (0, 1):
        return True

    # Calculate the square root
    root = math.isqrt(int(number))

    # Check if the square of the root equals the original number
    return root * root == number