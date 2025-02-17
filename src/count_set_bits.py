def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in the binary representation of an integer.
    
    Args:
        n (int): The input integer to count set bits in.
    
    Returns:
        int: The number of set bits in the integer.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle negative numbers by converting to unsigned 
    if n < 0:
        n = abs(n)
    
    # Count set bits using bitwise operations
    count = 0
    while n:
        count += n & 1  # Check least significant bit
        n >>= 1  # Right shift to check next bit
    
    return count