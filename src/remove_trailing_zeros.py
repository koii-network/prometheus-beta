def remove_trailing_zeros(number):
    """
    Remove all trailing zeros from the end of a non-negative integer.
    
    Args:
        number (int): A non-negative integer to remove trailing zeros from.
    
    Returns:
        int: The number with trailing zeros removed.
    
    Raises:
        ValueError: If the input is not a non-negative integer.
    """
    # Validate input
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if number == 0:
        return 0
    
    # Remove trailing zeros by integer division
    while number % 10 == 0:
        number //= 10
    
    return number