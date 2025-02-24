def calculate_lcm(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Least Common Multiple of a and b
    
    Raises:
        TypeError: If inputs are not integers
        ValueError: If inputs are negative
    """
    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Validate non-negative inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative")
    
    # Handle special cases
    if a == 0 or b == 0:
        return 0
    
    # Calculate LCM using GCD
    def gcd(x, y):
        """Helper function to calculate Greatest Common Divisor using Euclidean algorithm"""
        while y:
            x, y = y, x % y
        return x
    
    return abs(a * b) // gcd(a, b)