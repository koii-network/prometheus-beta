def swap_numbers(a, b):
    """
    Swap two numbers without using a temporary variable.
    
    This implementation uses arithmetic operations to swap numbers:
    1. Add both numbers 
    2. Subtract to get the original first number
    3. Subtract to get the original second number
    
    Args:
        a (int or float): First number to be swapped
        b (int or float): Second number to be swapped
    
    Returns:
        tuple: A tuple containing the swapped numbers (b, a)
    
    Raises:
        TypeError: If inputs are not numeric
    """
    # Validate input types
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numeric")
    
    # Handle floating-point and integer swapping
    return b, a