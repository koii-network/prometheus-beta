def gcd_recursive(a, b):
    """Calculate the Greatest Common Divisor (GCD) recursively using Euclidean algorithm."""
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)

def lcm_recursive(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers using recursion.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is zero
        TypeError: If inputs are not integers
    """
    # Type checking
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Zero check
    if a == 0 or b == 0:
        raise ValueError("LCM is undefined for zero")
    
    # LCM(a,b) = |a * b| / GCD(a,b)
    return abs((a * b) // gcd_recursive(a, b))