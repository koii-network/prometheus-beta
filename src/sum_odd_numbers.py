def sum_odd_numbers(n):
    """
    Calculate the sum of all odd numbers between 1 and n (inclusive).
    
    Args:
        n (int): The upper bound of the range.
    
    Returns:
        int: The sum of all odd numbers from 1 to n.
    
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Validate input is non-negative
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Use range() to generate odd numbers and sum() to calculate their total
    return sum(range(1, n + 1, 2))