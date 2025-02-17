def swap_numbers_arithmetic(a, b):
    """
    Swap two numbers using arithmetic operations without a temporary variable.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        tuple: Swapped numbers (b, a)
    """
    a = a + b  # a now contains sum of both numbers
    b = a - b  # b gets original value of a
    a = a - b  # a gets original value of b
    return a, b

def swap_numbers_bitwise(a, b):
    """
    Swap two numbers using bitwise XOR operation without a temporary variable.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        tuple: Swapped numbers (b, a)
    """
    a = a ^ b  # a now contains XOR of both numbers
    b = a ^ b  # b gets original value of a
    a = a ^ b  # a gets original value of b
    return a, b