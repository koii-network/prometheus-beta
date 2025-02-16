def gcd_recursive(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using recursion.
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is negative
    """
    # Validate input
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Base cases
    if b == 0:
        return a
    
    # Recursive case using Euclidean algorithm
    return gcd_recursive(b, a % b)