def count_triangular_numbers(n):
    """
    Count the number of triangular numbers less than or equal to n.
    
    A triangular number is a number that can be represented as a triangular 
    grid of points where the first row contains a single element and each 
    subsequent row contains one more element than the previous one.
    
    Args:
        n (int): The upper limit to count triangular numbers.
    
    Returns:
        int: The count of triangular numbers less than or equal to n.
    
    Raises:
        ValueError: If n is negative.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Triangular numbers follow the formula: k * (k + 1) / 2
    # We'll count how many such numbers are less than or equal to n
    count = 0
    k = 1
    
    while True:
        triangular_num = k * (k + 1) // 2
        
        if triangular_num > n:
            break
        
        count += 1
        k += 1
    
    return count