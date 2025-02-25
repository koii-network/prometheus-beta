def recursive_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using recursion.
    
    This implementation uses the Euclidean algorithm recursively:
    - If b is 0, return a (base case)
    - Otherwise, recursively call with b and the remainder of a divided by b
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is negative
    """
    # Validate inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: GCD(a, b) = GCD(b, a % b)
    return recursive_gcd(b, a % b)