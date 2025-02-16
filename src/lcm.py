def calculate_lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs are positive integers
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Both inputs must be positive integers")
    
    # Calculate GCD (Greatest Common Divisor) using Euclidean algorithm
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    # LCM formula: LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd(a, b)