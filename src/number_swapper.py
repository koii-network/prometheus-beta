def swap_numbers_arithmetic(a, b):
    """
    Swap two numbers using arithmetic operations without a temporary variable.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        tuple: A tuple containing the swapped numbers (b, a)
    """
    a = a + b  # a now becomes the sum of both numbers
    b = a - b  # b becomes the original value of a
    a = a - b  # a becomes the original value of b
    return a, b

def swap_numbers_bitwise(a, b):
    """
    Swap two numbers using bitwise XOR operations without a temporary variable.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        tuple: A tuple containing the swapped numbers (b, a)
    """
    a = a ^ b  # XOR a and b, store in a
    b = a ^ b  # XOR the new a with b gives original a
    a = a ^ b  # XOR the new a with new b gives original b
    return a, b