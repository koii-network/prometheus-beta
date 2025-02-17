def find_rightmost_set_bit(n):
    """
    Determine the position of the rightmost set bit in a number.
    
    Args:
        n (int): The input integer number.
    
    Returns:
        int: The position of the rightmost set bit (1-indexed).
             Returns 0 if no set bit is found (for input 0).
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle zero as a special case
    if n == 0:
        return 0
    
    # Use bitwise operations to find rightmost set bit
    position = 1
    while n > 0:
        if n & 1:  # Check if least significant bit is 1
            return position
        n >>= 1  # Right shift the number
        position += 1
    
    return 0  # This line should never be reached due to earlier checks