def find_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not an integer or if both inputs are zero
        TypeError: If inputs are not integers
    """
    # Validate input types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Handle special case where both inputs are zero
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined when both inputs are zero")
    
    # Take absolute values to handle negative numbers
    a, b = abs(a), abs(b)
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a