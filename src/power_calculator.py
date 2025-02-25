def recursive_power(base: float, exponent: int) -> float:
    """
    Calculate the power of a number using recursion.
    
    Args:
        base (float): The base number to be raised to a power
        exponent (int): The exponent (power) to raise the base to
    
    Returns:
        float: The result of base raised to the exponent
    
    Raises:
        ValueError: If exponent is negative
        TypeError: If base or exponent is not a number
    """
    # Type checking
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    # Handle special cases
    if exponent < 0:
        raise ValueError("Exponent cannot be negative")
    
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    # Recursive case
    return base * recursive_power(base, exponent - 1)