def swap_numbers(a, b):
    """
    Swap two numbers without using a temporary variable using bitwise XOR operation.
    
    Args:
        a (int): First number to be swapped
        b (int): Second number to be swapped
    
    Returns:
        tuple: A tuple containing the swapped numbers (b, a)
    
    Raises:
        TypeError: If inputs are not integers
    """
    # Type checking to ensure inputs are integers
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both inputs must be integers")
    
    # Swap using bitwise XOR operations
    a = a ^ b  # a now contains a XOR b
    b = a ^ b  # b now contains original a 
    a = a ^ b  # a now contains original b
    
    return (a, b)