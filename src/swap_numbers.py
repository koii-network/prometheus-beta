def swap_numbers(a, b):
    """
    Swap two numbers without using a temporary variable.
    
    Args:
        a (int): First number to be swapped
        b (int): Second number to be swapped
    
    Returns:
        tuple: A tuple containing the swapped numbers (b, a)
    """
    # Using arithmetic operations to swap numbers
    a = a + b  # a now becomes the sum of both numbers
    b = a - b  # b becomes the original value of a
    a = a - b  # a becomes the original value of b
    
    return a, b