def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using recursion.
    
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
    
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: call gcd with b and the remainder of a divided by b
    return gcd(b, a % b)