def is_power_of_two(n):
    """
    Check if a given number is a power of two.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is a power of two, False otherwise.
    
    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.
    """
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check for non-negative input
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0 and 1
    if n <= 1:
        return n == 1
    
    # Use bitwise operation to check if n is a power of two
    # A power of two has only one bit set in its binary representation
    # Subtracting 1 from a power of two will create a number with all lower bits set
    # So (n & (n-1)) will be 0 for powers of two
    return (n & (n-1)) == 0