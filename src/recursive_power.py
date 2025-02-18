def recursive_power(base, exponent):
    """
    Calculate the power of a number using recursion.
    
    Args:
        base (int/float): The base number
        exponent (int): The exponent (non-negative integer)
    
    Returns:
        int/float: Base raised to the power of exponent
    
    Raises:
        ValueError: If exponent is negative
    """
    # Handle base cases
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")
    
    # Base case for exponent 0
    if exponent == 0:
        return 1
    
    # Base case for exponent 1
    if exponent == 1:
        return base
    
    # Recursive case: base^exponent = base * base^(exponent-1)
    return base * recursive_power(base, exponent - 1)