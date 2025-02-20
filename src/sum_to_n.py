def sum_to_n(n: int) -> int:
    """
    Calculate the sum of all numbers from 1 to n in constant time.
    
    Args:
        n (int): A positive integer representing the upper limit of the sum.
    
    Returns:
        int: The sum of all integers from 1 to n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    return n * (n + 1) // 2