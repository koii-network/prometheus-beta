def recursive_power(base, exponent):
    """
    Calculate the power of a number using recursion.
    
    Args:
        base (int/float): The base number to be raised to a power
        exponent (int): The exponent (power) to raise the base to
    
    Returns:
        int/float: Base raised to the power of exponent
    
    Raises:
        ValueError: If exponent is negative
        TypeError: If base or exponent are not numbers
    """
    # Type checking
    if not (isinstance(base, (int, float)) and isinstance(exponent, int)):
        raise TypeError("Base must be a number and exponent must be an integer")
    
    # Handle base cases
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    
    if exponent == 0:
        return 1
    
    if exponent == 1:
        return base
    
    # Recursive case
    return base * recursive_power(base, exponent - 1)