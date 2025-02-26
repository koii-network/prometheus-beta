def find_matrix_coordinates(matrix, target):
    """
    Find the coordinates of a target value in a 2D matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix (list of lists) to search through
        target (int): The value to find in the matrix
    
    Returns:
        tuple: A tuple of (row, column) coordinates if found, or None if not found
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not of a comparable type
        ValueError: If the matrix is empty or contains inconsistent row lengths
    """
    # Validate input matrix
    if not matrix or not isinstance(matrix, list):
        raise ValueError("Matrix must be a non-empty list of lists")
    
    # Check matrix consistency
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("All rows in the matrix must have the same length")
    
    # Search through the matrix
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == target:
                return (row_idx, col_idx)
    
    # Target not found
    return None