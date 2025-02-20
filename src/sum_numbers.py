def sum_numbers(n: int) -> int:
    """
    Calculate the sum of all numbers from 1 to n in constant time.
    
    Args:
        n (int): The upper limit of the sum calculation.
    
    Returns:
        int: The sum of all numbers from 1 to n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    return n * (n + 1) // 2