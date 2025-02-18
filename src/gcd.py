def euclidean_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is negative
        TypeError: If inputs are not integers
    """
    # Check input types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Check for non-negative inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Base case: if one number is 0, return the other number
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm: repeatedly replace the larger number 
    # with the remainder of division until the remainder is 0
    while b != 0:
        a, b = b, a % b
    
    return a