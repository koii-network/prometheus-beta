def is_power_of_two(n):
    """
    Check if a given number is a power of two.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is a power of two, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.
    """
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check for non-negative numbers
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0 and 1
    if n == 0:
        return False
    if n == 1:
        return True
    
    # Bit manipulation method: 
    # A power of two will have only one bit set in its binary representation
    # n & (n-1) will clear the least significant bit
    # If n is a power of two, this operation will result in 0
    return (n & (n-1)) == 0