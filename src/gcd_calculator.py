def calculate_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two positive integers 
    using the Euclidean algorithm.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate input
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Euclidean algorithm using modulo for efficiency
    while b:
        a, b = b, a % b
    
    return a