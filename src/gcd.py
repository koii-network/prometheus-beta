def euclidean_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    Args:
        a (int): First integer 
        b (int): Second integer
    
    Returns:
        int: The Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs are positive integers
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    
    # Take absolute values to handle negative inputs
    a, b = abs(a), abs(b)
    
    # Base case: if b is 0, return a
    while b != 0:
        # Replace a with b, and b with the remainder of a divided by b
        a, b = b, a % b
    
    return a