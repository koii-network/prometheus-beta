def sum_to_n(n: int) -> int:
    """
    Calculate the sum of all numbers from 1 to n in constant time.
    
    Uses the mathematical formula: sum = n * (n + 1) / 2
    
    Args:
        n (int): A positive integer
    
    Returns:
        int: Sum of all numbers from 1 to n
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    return n * (n + 1) // 2  # Using integer division to avoid float conversion