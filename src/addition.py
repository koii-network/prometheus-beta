def add_without_plus(a, b):
    """
    Implement addition without using the + operator.
    
    Args:
        a (int): First number to add
        b (int): Second number to add
    
    Returns:
        int: Sum of a and b
    
    Raises:
        TypeError: If inputs are not integers
    """
    # Check input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both arguments must be integers")
    
    while b != 0:
        # Use bitwise operations to simulate addition
        # Carry contains common set bits of a and b
        carry = a & b
        
        # Sum without considering carry
        a = a ^ b
        
        # Shift carry left by 1 to add in next iteration
        b = carry << 1
    
    return a