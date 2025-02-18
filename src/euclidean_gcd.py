def gcd(a: int, b: int) -> int:
    """
    Implement the Euclidean algorithm to find the Greatest Common Divisor (GCD) of two numbers.
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is negative
    """
    # Validate inputs are non-negative
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Handle special case where one number is 0
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Apply Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    
    return a