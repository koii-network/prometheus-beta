def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1's) in the binary representation of an integer.
    
    Args:
        n (int): The input integer to count set bits.
    
    Returns:
        int: Number of set bits in the binary representation of the input integer.
    
    Examples:
        >>> count_set_bits(7)  # Binary: 111
        3
        >>> count_set_bits(0)  # Binary: 0
        0
        >>> count_set_bits(15)  # Binary: 1111
        4
    """
    # Check if input is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Use built-in bin() to convert to binary string and count '1's
    return bin(n).count('1')