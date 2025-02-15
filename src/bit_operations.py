def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in the binary representation of an integer.
    
    Args:
        n (int): The input integer to count set bits for.
    
    Returns:
        int: The number of set bits in the binary representation of the input.
    
    Examples:
        >>> count_set_bits(7)  # Binary: 111
        3
        >>> count_set_bits(0)
        0
        >>> count_set_bits(16)  # Binary: 10000
        1
    """
    # Handle negative numbers by converting to unsigned 
    if n < 0:
        n = abs(n)
    
    # Use bit manipulation to count set bits
    count = 0
    while n:
        count += n & 1  # Check if least significant bit is 1
        n >>= 1  # Right shift by 1 bit
    
    return count