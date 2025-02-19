def sum_odd_numbers(n):
    """
    Calculate the sum of all odd numbers between 1 and n (inclusive).
    
    Args:
        n (int): Upper bound of the range to sum odd numbers.
    
    Returns:
        int: Sum of all odd numbers from 1 to n.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Use range() to generate odd numbers and sum() to calculate their total
    return sum(range(1, n + 1, 2))