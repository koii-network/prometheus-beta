def find_rightmost_set_bit(n: int) -> int:
    """
    Determine the position of the rightmost set bit (1) in a number.
    
    Args:
        n (int): The input integer to check for the rightmost set bit.
    
    Returns:
        int: The position of the rightmost set bit (1-indexed), 
             or 0 if no set bit exists.
    
    Raises:
        TypeError: If the input is not an integer.
    
    Examples:
        >>> find_rightmost_set_bit(18)  # 18 is 10010 in binary
        2
        >>> find_rightmost_set_bit(0)
        0
        >>> find_rightmost_set_bit(1)
        1
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle 0 as a special case
    if n == 0:
        return 0
    
    # Use bitwise operations to find the rightmost set bit
    # The formula uses n & -n to isolate the rightmost set bit
    return (n & -n).bit_length()