def add_matrices(matrix1, matrix2):
    """
    Add two matrices by adding corresponding elements.
    
    Args:
        matrix1 (list of lists): First input matrix
        matrix2 (list of lists): Second input matrix
    
    Returns:
        list of lists: Resulting matrix after addition
    
    Raises:
        ValueError: If matrices have incompatible dimensions
    """
    # Check if matrices are empty
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")
    
    # Check matrix dimensions
    if len(matrix1) != len(matrix2):
        raise ValueError("Matrices must have the same number of rows")
    
    # Check column dimensions
    if any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("Matrices must have the same number of columns in each row")
    
    # Perform matrix addition
    result = []
    for row1, row2 in zip(matrix1, matrix2):
        result_row = [a + b for a, b in zip(row1, row2)]
        result.append(result_row)
    
    return result