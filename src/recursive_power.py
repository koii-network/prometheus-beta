def recursive_power(base, exponent):
    """
    Calculate the power of a number using recursion.
    
    Args:
        base (int/float): The base number
        exponent (int): The exponent (non-negative integer)
    
    Returns:
        int/float: base raised to the power of exponent
    
    Raises:
        ValueError: If exponent is negative
    """
    # Handle edge cases
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    # Recursive case
    return base * recursive_power(base, exponent - 1)