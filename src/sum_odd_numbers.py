def sum_odd_numbers(n):
    """
    Calculate the sum of all odd numbers between 1 and n (inclusive).
    
    Args:
        n (int): The upper limit for finding odd numbers.
    
    Returns:
        int: Sum of all odd numbers from 1 to n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Use range with step 2 to get only odd numbers, sum them up
    return sum(range(1, n + 1, 2))