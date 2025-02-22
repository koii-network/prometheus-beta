def euclidean_gcd(a: int, b: int) -> int:
    """
    Implements the Euclidean algorithm to find the Greatest Common Divisor (GCD)
    of two non-negative integers.

    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer

    Returns:
        int: The greatest common divisor of a and b

    Raises:
        ValueError: If either input is negative
    """
    # Check for negative inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Handle special cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Apply Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a