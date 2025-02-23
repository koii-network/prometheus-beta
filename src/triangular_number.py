def calculate_triangular_number(n):
    """
    Calculate the nth triangular number.
    
    A triangular number is the sum of all positive integers from 1 to n.
    
    Args:
        n (int): The position of the triangular number to calculate.
    
    Returns:
        int: The nth triangular number.
    
    Raises:
        ValueError: If n is less than 0.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    return (n * (n + 1)) // 2