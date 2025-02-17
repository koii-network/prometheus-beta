def find_lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is less than or equal to 0
    """
    # Validate inputs
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive integers")
    
    # Helper function to calculate Greatest Common Divisor (GCD) using Euclidean algorithm
    def gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x
    
    # LCM formula: LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd(a, b)