def add_without_plus(a, b):
    """
    Implement addition without using the + operator.
    
    Args:
        a (int): First number to add
        b (int): Second number to add
    
    Returns:
        int: Sum of a and b
    """
    # Use bitwise operations to perform addition
    while b != 0:
        # Carry contains common set bits of a and b
        carry = a & b
        
        # Sum of bits of a and b where at least one bit is not set
        a = a ^ b
        
        # Shift carry by one so it can be added to next bit
        b = carry << 1
    
    return a