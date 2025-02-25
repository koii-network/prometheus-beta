def euclidean_gcd(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
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
    
    # Base case: if b is 0, return a
    while b != 0:
        # Swap and take remainder
        a, b = b, a % b
    
    return a