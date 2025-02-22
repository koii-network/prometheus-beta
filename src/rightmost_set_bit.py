def find_rightmost_set_bit(number):
    """
    Determine the position of the rightmost set bit in a number.
    
    Args:
        number (int): The input number to find the rightmost set bit.
    
    Returns:
        int: The position of the rightmost set bit (1-indexed), or 0 if no set bit exists.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Input validation
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if number == 0:
        return 0
    
    # Use bitwise operations to find the rightmost set bit
    position = 1
    while number > 0:
        if number & 1:
            return position
        number >>= 1
        position += 1
    
    return 0