def reverse_bits(num):
    """
    Reverse the bits of a given integer.
    
    Args:
        num (int): The input integer to have its bits reversed.
    
    Returns:
        int: An integer with the bits of the input reversed.
    
    Examples:
        >>> reverse_bits(43261596)  # Binary: 00000010100101000001111010011100
        964176192  # Binary: 00111001011110000010100101000000
        >>> reverse_bits(4294967295)  # All 1s
        4294967295  # All 1s
        >>> reverse_bits(0)  # Zero
        0
    """
    # Ensure 32-bit unsigned integer
    num = num & 0xFFFFFFFF
    
    # Initialize the reversed number
    reversed_num = 0
    
    # Iterate through all 32 bits
    for i in range(32):
        # Extract the least significant bit
        current_bit = (num >> i) & 1
        
        # Place this bit in the reversed position
        reversed_num |= (current_bit << (31 - i))
    
    return reversed_num