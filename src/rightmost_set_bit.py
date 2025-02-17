def find_rightmost_set_bit(n):
    """
    Determine the position of the rightmost set bit in a number.
    
    Args:
        n (int): The input number to check.
    
    Returns:
        int: The position of the rightmost set bit (1-indexed).
             Returns 0 if no set bit is found.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Negative number check
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # If number is 0, no set bit exists
    if n == 0:
        return 0
    
    # Use bitwise operations to find the rightmost set bit
    # This works by using the two's complement trick
    # (n & -n) isolates the rightmost set bit
    rightmost_bit = n & -n
    
    # Calculate the position using log2 and bit manipulation
    position = 1
    while rightmost_bit > 1:
        rightmost_bit >>= 1
        position += 1
    
    return position