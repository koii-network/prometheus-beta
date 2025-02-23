def sparse_matrix_multiply(matrix1: dict, matrix2: dict) -> dict:
    """
    Perform sparse matrix multiplication using dictionary representation.
    
    Args:
        matrix1 (dict): First sparse matrix with row indices as keys and row vectors as values
        matrix2 (dict): Second sparse matrix with row indices as keys and row vectors as values
    
    Returns:
        dict: Resulting sparse matrix from multiplication
    
    Raises:
        ValueError: If matrices cannot be multiplied (incompatible dimensions)
    """
    # Check if matrices can be multiplied
    if not matrix1 or not matrix2:
        return {}
    
    # Validate matrix dimensions
    matrix1_cols = max(max(row.keys()) + 1 if row else 0 for row in matrix1.values()) if matrix1 else 0
    matrix2_rows = len(matrix2)
    
    if matrix1_cols != matrix2_rows:
        raise ValueError("Matrix dimensions are incompatible for multiplication")
    
    # Compute result matrix
    result = {}
    
    for i, row1 in matrix1.items():
        result[i] = {}
        for j in range(max(matrix2.keys()) + 1):
            # Compute dot product for current element
            dot_product = 0
            for k, val1 in row1.items():
                if k in matrix2.get(j, {}):
                    dot_product += val1 * matrix2[j][k]
            
            # Only store non-zero elements
            if dot_product != 0:
                result[i][j] = dot_product
        
        # Remove empty rows
        if not result[i]:
            del result[i]
    
    return result