def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a given 32-bit unsigned integer.
    
    Args:
        n (int): A 32-bit unsigned integer to be bit-reversed.
    
    Returns:
        int: The number with its bits reversed.
    
    Examples:
        >>> reverse_bits(43261596)  # 00000010100101000001111010011100 (input)
        964176192  # 00111001011110000010100101000000 (output)
        >>> reverse_bits(4294967295)  # All 1s
        4294967295  # All 1s (symmetric)
    """
    # Ensure the input is a 32-bit unsigned integer
    n = n & 0xFFFFFFFF
    
    # Reverse the bits systematically
    n = ((n & 0xffff0000) >> 16) | ((n & 0x0000ffff) << 16)  # Swap 16-bit halves
    n = ((n & 0xff00ff00) >> 8)  | ((n & 0x00ff00ff) << 8)   # Swap 8-bit groups
    n = ((n & 0xf0f0f0f0) >> 4)  | ((n & 0x0f0f0f0f) << 4)   # Swap 4-bit groups
    n = ((n & 0xcccccccc) >> 2)  | ((n & 0x33333333) << 2)   # Swap 2-bit groups
    n = ((n & 0xaaaaaaaa) >> 1)  | ((n & 0x55555555) << 1)   # Swap individual bits
    
    return n