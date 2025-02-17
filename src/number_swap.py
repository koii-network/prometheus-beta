def swap_numbers(a, b):
    """
    Swap two numbers without using a temporary variable.
    
    Uses arithmetic operations to swap numbers in-place.
    
    Args:
        a (int): First number to be swapped
        b (int): Second number to be swapped
    
    Returns:
        tuple: A tuple containing the swapped numbers (b, a)
    """
    # Perform swap using arithmetic operations
    a = a + b  # a now contains sum of both numbers
    b = a - b  # b gets original value of a 
    a = a - b  # a gets original value of b
    
    return a, b