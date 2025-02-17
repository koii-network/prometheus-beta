def find_rightmost_set_bit(n):
    """
    Determine the position of the rightmost set bit in a number.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: The position of the rightmost set bit (1-indexed)
             Returns 0 if no set bit is found (for input 0)
    
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
    """
    # Validate input
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
        if n & 1:
            return position
        n >>= 1
        position += 1
    
    return 0