import random

def generate_random_integer(start: int, end: int) -> int:
    """
    Generate a random integer within the specified inclusive range.

    Args:
        start (int): The lower bound of the range (inclusive).
        end (int): The upper bound of the range (inclusive).

    Returns:
        int: A random integer between start and end (inclusive).

    Raises:
        ValueError: If start is greater than end.
        TypeError: If start or end are not integers.
    """
    # Validate input types
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both start and end must be integers")
    
    # Validate range
    if start > end:
        raise ValueError("Start value must be less than or equal to end value")
    
    # Generate and return random integer in the specified range
    return random.randint(start, end)