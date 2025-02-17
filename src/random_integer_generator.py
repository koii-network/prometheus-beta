import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within the specified range (inclusive).
    
    Args:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.
    
    Returns:
        int: A random integer between min_value and max_value (inclusive).
    
    Raises:
        ValueError: If min_value is greater than max_value.
        TypeError: If inputs are not integers.
    """
    # Validate input types
    if not isinstance(min_value, int) or not isinstance(max_value, int):
        raise TypeError("Both min_value and max_value must be integers")
    
    # Validate range
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value")
    
    # Generate and return random integer
    return random.randint(min_value, max_value)