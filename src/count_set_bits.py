def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in the binary representation of an integer.
    
    Args:
        n (int): The input integer to count set bits for.
    
    Returns:
        int: The number of set bits in the input integer.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle negative numbers by converting to unsigned 
    if n < 0:
        n = abs(n)
    
    # Initialize bit count
    bit_count = 0
    
    # Count set bits using bitwise AND
    while n:
        bit_count += n & 1  # Check least significant bit
        n >>= 1  # Right shift to check next bit
    
    return bit_count