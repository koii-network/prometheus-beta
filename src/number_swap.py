def swap_numbers(a, b):
    """
    Swap two numbers without using a temporary variable.
    
    This implementation uses arithmetic operations to swap numbers:
    1. Add both numbers 
    2. Subtract to get the original first number
    3. Subtract to get the original second number
    
    Args:
        a (int): First number to be swapped
        b (int): Second number to be swapped
    
    Returns:
        tuple: A tuple containing the swapped numbers (b, a)
    
    Raises:
        TypeError: If inputs are not numeric
    """
    # Validate input types
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numeric")
    
    # Swap numbers using arithmetic operations
    a = a + b  # a now contains sum of both numbers
    b = a - b  # b gets original value of a
    a = a - b  # a gets original value of b
    
    return a, b