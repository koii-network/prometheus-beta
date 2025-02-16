def calculate_lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    
    Args:
        a (int): First integer number
        b (int): Second integer number
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is less than 1
    """
    # Check for valid input
    if a < 1 or b < 1:
        raise ValueError("Inputs must be positive integers")
    
    # Helper function to calculate GCD using Euclidean algorithm
    def gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x
    
    # LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd(a, b)