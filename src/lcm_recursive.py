def calculate_lcm_recursive(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers using recursion.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Input validation
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Base case: if one number divides the other, return the larger number
    if a % b == 0:
        return a
    if b % a == 0:
        return b
    
    # Recursive case: use the identity LCM(a,b) = |a*b| / GCD(a,b)
    def gcd_recursive(x, y):
        """Helper function to calculate GCD recursively"""
        if y == 0:
            return x
        return gcd_recursive(y, x % y)
    
    return abs(a * b) // gcd_recursive(a, b)