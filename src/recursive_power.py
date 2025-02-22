def recursive_power(base: float, exponent: int) -> float:
    """
    Calculate the power of a number using recursion.
    
    Args:
        base (float): The base number
        exponent (int): The exponent (power) to raise the base to
    
    Returns:
        float: base raised to the power of exponent
    
    Raises:
        ValueError: If exponent is negative
    """
    # Handle edge cases
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    if exponent < 0:
        raise ValueError("Exponent cannot be negative")
    
    # Base cases
    if exponent == 0:
        return 1.0
    
    if exponent == 1:
        return base
    
    # Recursive case
    if exponent % 2 == 0:
        # For even exponents, use efficiency optimization
        half_power = recursive_power(base, exponent // 2)
        return half_power * half_power
    else:
        # For odd exponents
        return base * recursive_power(base, exponent - 1)