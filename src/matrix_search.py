def matrix_search(matrix, target):
    """
    Search for a target value in a 2D matrix and return its coordinates.
    
    Args:
        matrix (List[List[int]]): A 2D matrix to search through
        target (int): The value to find in the matrix
    
    Returns:
        tuple: A tuple of (row, col) coordinates if found, or None if not found
    
    Raises:
        TypeError: If matrix is not a valid 2D list or target is not a comparable type
    """
    # Validate input
    if not matrix or not matrix[0]:
        return None
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a 2D list")
    
    # Get matrix dimensions
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Perform search
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == target:
                return (row, col)
    
    # Target not found
    return None