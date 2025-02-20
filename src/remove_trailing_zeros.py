def remove_trailing_zeros(num):
    """
    Remove all trailing zeros from the end of a non-negative integer.
    
    Args:
        num (int): A non-negative integer
    
    Returns:
        int: The number with trailing zeros removed
    
    Raises:
        ValueError: If input is not a non-negative integer
    """
    # Validate input
    if not isinstance(num, int) or num < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if num == 0:
        return 0
    
    # Remove trailing zeros
    while num % 10 == 0:
        num //= 10
    
    return num