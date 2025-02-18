def gcd_recursive(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) using recursion.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Greatest Common Divisor of a and b
    """
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: use the Euclidean algorithm
    return gcd_recursive(b, a % b)

def lcm_recursive(a, b):
    """
    Calculate the Least Common Multiple (LCM) using recursion.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate input
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd_recursive(a, b)