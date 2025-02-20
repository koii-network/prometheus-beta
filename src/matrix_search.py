def matrix_search(matrix, target):
    """
    Search for a target value in a 2D matrix and return its coordinates.
    
    Args:
        matrix (List[List[int]]): A 2D matrix to search through
        target (int): The value to find in the matrix
    
    Returns:
        Tuple[int, int] or None: Coordinates (row, col) of the target, 
        or None if not found
    
    Raises:
        TypeError: If input is not a valid 2D matrix
        ValueError: If matrix is empty
    """
    # Validate input
    if not matrix or not isinstance(matrix, list):
        raise ValueError("Matrix must be a non-empty 2D list")
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a 2D matrix")
    
    # Check if all rows have consistent length
    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("All rows in the matrix must have the same length")
    
    # Iterate through the matrix to find the target
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == target:
                return (row_idx, col_idx)
    
    # Target not found
    return None