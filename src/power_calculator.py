def recursive_power(base: float, exponent: int) -> float:
    """
    Calculate the power of a number using recursion.
    
    Args:
        base (float): The base number to be raised to a power.
        exponent (int): The exponent (power) to raise the base to.
    
    Returns:
        float: The result of base raised to the exponent.
    
    Raises:
        TypeError: If base is not a number or exponent is not an integer.
        ValueError: If exponent is negative.
    """
    # Type checking
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    # Handle special cases
    if exponent < 0:
        raise ValueError("Exponent must be non-negative for this implementation")
    
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    # Recursive case
    return base * recursive_power(base, exponent - 1)