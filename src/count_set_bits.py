def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1's) in the binary representation of an integer.
    
    Args:
        n (int): The input integer to count set bits for.
    
    Returns:
        int: The number of set bits in the binary representation of the input.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle negative numbers by converting to unsigned 
    if n < 0:
        n = n & ((1 << 64) - 1)  # Handle 64-bit signed integer conversion
    
    # Count set bits using Brian Kernighan's Algorithm
    count = 0
    while n:
        n &= (n - 1)  # Clear the least significant set bit
        count += 1
    
    return count