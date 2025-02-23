def count_triangular_numbers(n):
    """
    Count the number of triangular numbers less than or equal to n.
    
    A triangular number is a number that can be represented as a triangular 
    grid of points where the first row contains a single element and each 
    subsequent row contains one more element than the previous one.
    
    Triangular numbers follow the formula: T(k) = k * (k + 1) // 2
    
    Args:
        n (int): The upper limit to count triangular numbers.
    
    Returns:
        int: The count of triangular numbers less than or equal to n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    count = 0
    k = 1
    triangular_num = 1
    
    while triangular_num <= n:
        count += 1
        k += 1
        triangular_num = k * (k + 1) // 2
    
    return count