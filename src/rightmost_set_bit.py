def find_rightmost_set_bit(n):
    """
    Determine the position of the rightmost set bit in a number.
    
    Args:
        n (int): The input number to check.
    
    Returns:
        int: The position of the rightmost set bit (1-indexed), 
             or 0 if no set bits are found.
    
    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.
    """
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check for negative input
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle special case of 0
    if n == 0:
        return 0
    
    # Use bitwise operation to find rightmost set bit
    position = 1
    while n > 0:
        # Check if least significant bit is 1
        if n & 1:
            return position
        
        # Right shift and increment position
        n >>= 1
        position += 1
    
    return 0