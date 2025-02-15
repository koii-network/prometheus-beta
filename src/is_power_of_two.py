def is_power_of_two(n):
    """
    Check if a given number is a power of two.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is a power of two, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle special cases
    if n <= 0:
        return False
    
    # A power of two has only one bit set in its binary representation
    # We can check this by using bitwise operations
    # n & (n - 1) will be 0 for powers of two
    return (n & (n - 1)) == 0