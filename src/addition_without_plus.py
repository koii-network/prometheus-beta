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
        # Carry stores the common set bits
        carry = a & b
        
        # Sum without considering carry
        a = a ^ b
        
        # Shift carry left by 1 to add in next iteration
        b = carry << 1
    
    return a