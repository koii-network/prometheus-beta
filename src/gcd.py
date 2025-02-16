def find_gcd(a: int, b: int) -> int:
    """
    Find the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    # Take absolute values to handle negative numbers
    a, b = abs(a), abs(b)
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a