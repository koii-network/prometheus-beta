def matrix_search(matrix, target):
    """
    Find the coordinates of a target value in a 2D matrix.
    
    Args:
        matrix (list of lists): A 2D matrix to search through
        target (any): The value to find in the matrix
    
    Returns:
        tuple: A tuple of (row, col) coordinates if found, or None if not found
    
    Raises:
        TypeError: If matrix is not a valid 2D list or is empty
    """
    # Validate matrix input
    if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a non-empty 2D list")
    
    # Check for empty rows
    if not all(matrix):
        return None
    
    # Ensure consistent row lengths
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("All rows must have the same length")
    
    # Search through matrix
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == target:
                return (row_idx, col_idx)
    
    # Target not found
    return None