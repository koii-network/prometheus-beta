def euclidean_gcd(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    The Euclidean algorithm is based on the principle that the greatest common divisor 
    of two numbers does not change if the smaller number is subtracted from the larger number.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The Greatest Common Divisor of a and b
    
    Raises:
        TypeError: If inputs are not integers
        ValueError: If inputs are negative
    """
    # Check input types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Check for negative inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Handle special cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm implementation
    while b:
        a, b = b, a % b
    
    return a