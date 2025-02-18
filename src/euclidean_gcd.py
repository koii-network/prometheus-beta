def euclidean_gcd(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    Args:
        a (int): First integer 
        b (int): Second integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs are positive integers
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    
    # Take absolute values to handle negative inputs
    a, b = abs(a), abs(b)
    
    # Handle special cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm: repeatedly replace the larger number 
    # with the remainder of the division until remainder is 0
    while b:
        a, b = b, a % b
    
    return a