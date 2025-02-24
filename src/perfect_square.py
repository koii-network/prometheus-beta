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
        TypeError: If the input is not a number.
        ValueError: If the input is negative.

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
    # Check input type
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")

    # Check for negative numbers
    if number < 0:
        raise ValueError("Input must be a non-negative number")

    # Special case for 0 and 1
    if number in (0, 1):
        return True

    # Calculate the square root
    sqrt = math.isqrt(int(number))

    # Check if the square of the integer square root equals the original number
    return sqrt * sqrt == number