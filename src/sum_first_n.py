def sum_first_n_integers(n: int) -> int:
    """
    Calculate the sum of all integers from 1 to n in constant time using the mathematical formula.
    
    This function uses the arithmetic series sum formula: sum = n * (n + 1) / 2,
    which allows for O(1) time complexity.
    
    Args:
        n (int): A non-negative integer representing the upper limit of the sum.
    
    Returns:
        int: The sum of all integers from 1 to n.
    
    Raises:
        ValueError: If n is negative.
    
    Examples:
        >>> sum_first_n_integers(5)
        15
        >>> sum_first_n_integers(0)
        0
    """
    # Check for negative input
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Use the mathematical formula for sum of first n integers
    return n * (n + 1) // 2