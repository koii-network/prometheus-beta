def find_lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two integers.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: The least common multiple of a and b

    Raises:
        ValueError: If either input is less than or equal to zero
    """
    # Validate inputs
    if a <= 0 or b <= 0:
        raise ValueError("Both inputs must be positive integers")

    # Use the formula: LCM(a,b) = |a * b| / GCD(a,b)
    def gcd(x: int, y: int) -> int:
        """Helper function to calculate Greatest Common Divisor using Euclidean algorithm"""
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)