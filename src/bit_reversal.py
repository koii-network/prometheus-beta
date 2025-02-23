def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a given 32-bit unsigned integer.
    
    Args:
        n (int): A 32-bit unsigned integer to reverse bits for.
    
    Returns:
        int: The number with its bits reversed.
    
    Raises:
        ValueError: If the input is not a non-negative 32-bit integer.
    
    Examples:
        >>> reverse_bits(43261596)  # 00000010100101000001111010011100
        964176192                   # 00111001011110000010100101000000
    """
    # Validate input
    if not isinstance(n, int) or n < 0 or n > 0xFFFFFFFF:
        raise ValueError("Input must be a 32-bit unsigned integer")
    
    # Reverse bits using bit manipulation
    reversed_num = 0
    for i in range(32):
        # Left shift the reversed number and add the least significant bit of n
        reversed_num = (reversed_num << 1) | (n & 1)
        # Right shift n to check next bit
        n >>= 1
    
    return reversed_num