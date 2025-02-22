def find_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Check for valid inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    # Take absolute values to handle negative numbers
    a, b = abs(a), abs(b)
    
    # Special case: if either number is 0, return the other number
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a