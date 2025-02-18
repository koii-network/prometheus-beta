def calculate_triangular_number(n):
    """
    Calculate the nth triangular number.
    
    A triangular number is the sum of all positive integers from 1 to n.
    For example, the 4th triangular number is 1 + 2 + 3 + 4 = 10.
    
    Args:
        n (int): The position of the triangular number to calculate.
    
    Returns:
        int: The nth triangular number.
    
    Raises:
        ValueError: If n is less than 1.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Optimized formula: nth triangular number = n * (n + 1) // 2
    return n * (n + 1) // 2