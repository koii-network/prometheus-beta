def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a given 32-bit unsigned integer.
    
    Args:
        n (int): The input 32-bit unsigned integer to reverse.
    
    Returns:
        int: The integer with its bits reversed.
    
    Raises:
        ValueError: If the input is not a 32-bit unsigned integer.
    
    Examples:
        >>> reverse_bits(43261596)  # 00000010100101000001111010011100 -> 00111001011110000010100101000000
        964176192
        >>> reverse_bits(4294967295)  # All 1s
        4294967295
        >>> reverse_bits(0)  # All 0s
        0
    """
    # Check if the input is a valid 32-bit unsigned integer
    if not isinstance(n, int) or n < 0 or n > 0xFFFFFFFF:
        raise ValueError("Input must be a 32-bit unsigned integer (0 to 4294967295)")
    
    # Initialize the result
    reversed_num = 0
    
    # Reverse bits by shifting and masking
    for i in range(32):
        # Left shift the result and add the least significant bit of n
        reversed_num = (reversed_num << 1) | (n & 1)
        # Right shift n to examine the next bit
        n >>= 1
    
    return reversed_num