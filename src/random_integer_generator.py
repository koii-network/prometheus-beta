import random

def generate_random_integer(min_value: int, max_value: int) -> int:
    """
    Generate a random integer within a given range (inclusive).
    
    Args:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.
    
    Returns:
        int: A random integer between min_value and max_value (inclusive).
    
    Raises:
        ValueError: If min_value is greater than max_value.
    """
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")
    
    return random.randint(min_value, max_value)