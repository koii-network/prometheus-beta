def find_rightmost_set_bit_position(n):
    """
    Determine the position of the rightmost set bit in a number.
    
    Args:
        n (int): The input number to check.
    
    Returns:
        int: The position of the rightmost set bit (1-indexed),
             or 0 if no set bit is found.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Check input type and value
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if n == 0:
        return 0
    
    # Use bitwise operations to find the rightmost set bit
    position = 1
    while n > 0:
        if n & 1:  # Check if the least significant bit is 1
            return position
        n >>= 1   # Right shift to check next bit
        position += 1
    
    return 0  # This line should never be reached due to previous checks