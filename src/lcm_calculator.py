def calculate_lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    
    Args:
        a (int): First integer number
        b (int): Second integer number
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate input
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Calculate GCD using Euclidean algorithm
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    # LCM(a, b) = |a * b| / GCD(a, b)
    return abs(a * b) // gcd(a, b)