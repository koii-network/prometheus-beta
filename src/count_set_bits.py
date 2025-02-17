def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in the binary representation of an integer.
    
    Args:
        n (int): The input integer to count set bits in.
    
    Returns:
        int: The number of set bits in the input integer.
    
    Examples:
        >>> count_set_bits(7)   # 111 in binary
        3
        >>> count_set_bits(0)   # 0 in binary
        0
        >>> count_set_bits(15)  # 1111 in binary
        4
    """
    # Handle negative numbers by converting to unsigned 
    if n < 0:
        n = n & ((1 << 64) - 1)  # For 64-bit integers
    
    # Initialize set bit count
    count = 0
    
    # Iterate through all bits
    while n:
        # Check the least significant bit
        count += n & 1
        
        # Right shift to check next bit
        n >>= 1
    
    return count