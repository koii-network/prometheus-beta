def remove_trailing_zeros(number):
    """
    Remove all trailing zeros from a non-negative integer.
    
    Args:
        number (int): A non-negative integer.
    
    Returns:
        int: The number with all trailing zeros removed.
    
    Raises:
        ValueError: If the input is not a non-negative integer.
    """
    # Validate input
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # If number is 0, return 0
    if number == 0:
        return 0
    
    # Remove trailing zeros
    while number % 10 == 0:
        number //= 10
    
    return number