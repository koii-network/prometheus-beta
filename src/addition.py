def add_without_plus(a, b):
    """
    Implement addition without using the '+' operator.
    
    Uses bitwise operations to perform addition:
    - Uses bitwise XOR (^) to add without carrying
    - Uses bitwise AND (&) to handle carry
    - Recursively shifts carry until no carry remains
    
    Args:
        a (int): First number to add
        b (int): Second number to add
    
    Returns:
        int: Sum of a and b
    """
    # Handle base cases
    if b == 0:
        return a
    
    # Calculate sum without carry
    sum_without_carry = a ^ b
    
    # Calculate carry
    carry = (a & b) << 1
    
    # Recursively add sum without carry and carry
    return add_without_plus(sum_without_carry, carry)