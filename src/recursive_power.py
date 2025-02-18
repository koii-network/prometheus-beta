def calculate_power(base, exponent):
    """
    Calculate the power of a number using recursion.
    
    Args:
        base (int or float): The base number
        exponent (int): The exponent (non-negative integer)
    
    Returns:
        float or int: base raised to the power of exponent
    
    Raises:
        ValueError: If exponent is negative
    """
    # Check for invalid exponent
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    # Base cases
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    
    if exponent == 0:
        return 1
    
    if exponent == 1:
        return base
    
    # Recursive case
    return base * calculate_power(base, exponent - 1)