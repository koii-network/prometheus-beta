def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    The Euclidean algorithm is based on the principle that the greatest common divisor 
    of two numbers does not change if the smaller number is subtracted from the larger number.
    
    Args:
        a (int): First integer 
        b (int): Second integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    # Take absolute values to handle negative inputs
    a, b = abs(a), abs(b)
    
    # Handle special cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm 
    while b:
        a, b = b, a % b
    
    return a