def find_rightmost_set_bit(n: int) -> int:
    """
    Determine the position of the rightmost set bit (1) in a given number.
    
    Args:
        n (int): The input integer to check for the rightmost set bit.
    
    Returns:
        int: The position of the rightmost set bit (1-indexed), 
             or 0 if no set bit is found (for input 0).
    
    Raises:
        TypeError: If the input is not an integer.
    
    Examples:
        >>> find_rightmost_set_bit(18)  # Binary: 10010, rightmost set bit is at position 2
        2
        >>> find_rightmost_set_bit(0)   # No set bit
        0
        >>> find_rightmost_set_bit(1)   # Rightmost bit is at position 1
        1
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle edge case of 0
    if n == 0:
        return 0
    
    # Use bitwise operation to find the rightmost set bit
    # The formula works by taking the two's complement negative and 
    # performing bitwise AND with the original number
    position = (n & -n).bit_length()
    return position