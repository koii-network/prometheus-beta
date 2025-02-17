def swap_numbers(a, b):
    """
    Swap two numbers without using a temporary variable.
    
    This implementation uses arithmetic operations to swap the numbers.
    
    Args:
        a (int): First number to be swapped
        b (int): Second number to be swapped
    
    Returns:
        tuple: A tuple containing the swapped numbers (b, a)
    """
    # Check if the input values are the same
    if a == b:
        return (a, b)
    
    # Swap numbers using arithmetic operations
    a = a + b  # a now contains the sum of both numbers
    b = a - b  # b now contains the original value of a
    a = a - b  # a now contains the original value of b
    
    return (a, b)