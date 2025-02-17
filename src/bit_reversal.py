def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a given 32-bit unsigned integer.
    
    Args:
        n (int): A 32-bit unsigned integer to reverse bits
    
    Returns:
        int: The number with its bits reversed
    
    Example:
        >>> reverse_bits(43261596)  # 00000010100101000001111010011100
        964176192                   # 00111001011110000010100101000000
    """
    # Ensure the input is a 32-bit unsigned integer
    n = n & 0xFFFFFFFF
    
    # Bit manipulation trick to reverse bits
    n = ((n & 0xFFFF0000) >> 16) | ((n & 0x0000FFFF) << 16)
    n = ((n & 0xFF00FF00) >> 8)  | ((n & 0x00FF00FF) << 8)
    n = ((n & 0xF0F0F0F0) >> 4)  | ((n & 0x0F0F0F0F) << 4)
    n = ((n & 0xCCCCCCCC) >> 2)  | ((n & 0x33333333) << 2)
    n = ((n & 0xAAAAAAAA) >> 1)  | ((n & 0x55555555) << 1)
    
    return n