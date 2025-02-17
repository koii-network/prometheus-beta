def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a given 32-bit unsigned integer.
    
    Args:
        n (int): A 32-bit unsigned integer to reverse bits.
    
    Returns:
        int: The number with its bits reversed.
    
    Examples:
        >>> reverse_bits(43261596)  # 00000010100101000001111010011100 -> 00111001011110000010100101000000
        964176192
        >>> reverse_bits(4294967295)  # All 1s 
        4294967295
        >>> reverse_bits(0)  # All 0s
        0
    """
    # Ensure the input is a 32-bit unsigned integer
    n &= 0xFFFFFFFF
    
    # Initialize the result
    result = 0
    
    # Reverse bits by shifting
    for i in range(32):
        # Left shift the result and add the least significant bit of n
        result = (result << 1) | (n & 1)
        # Right shift n to process next bit
        n >>= 1
    
    return result