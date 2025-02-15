def add_without_plus(a, b):
    """
    Implement addition without using the + operator using bitwise operations.
    
    Args:
        a (int): First number to add
        b (int): Second number to add
    
    Returns:
        int: Sum of a and b
    """
    # Continue until there are no more carry bits
    while b != 0:
        # Calculate carry bits 
        carry = a & b
        
        # Calculate sum without considering carry
        a = a ^ b
        
        # Shift carry bits left by 1 
        b = carry << 1
    
    return a