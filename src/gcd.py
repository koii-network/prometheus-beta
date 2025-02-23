def find_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
    
    Args:
        a (int): First integer number
        b (int): Second integer number
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not an integer or is negative
    """
    # Validate input types and values
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Handle special cases
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    
    # Euclidean algorithm implementation
    while b:
        a, b = b, a % b
    
    return abs(a)