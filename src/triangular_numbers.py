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
        ValueError: If the input is not a non-negative integer.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    count = 0
    triangular_num = 0
    i = 1
    
    while triangular_num <= n:
        triangular_num = (i * (i + 1)) // 2
        if triangular_num <= n:
            count += 1
        i += 1
    
    return count