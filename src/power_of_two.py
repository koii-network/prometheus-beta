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
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if n < 0:
        raise ValueError("Input must be a non-negative number")
    
    # Special case: 0 is not a power of two
    if n == 0:
        return False
    
    # A number is a power of two if only one bit is set
    # This can be checked by the bitwise AND operation
    return (n & (n - 1)) == 0