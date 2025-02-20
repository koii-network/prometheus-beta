def sparse_matrix_multiply(matrix1, matrix2):
    """
    Perform sparse matrix multiplication using dictionaries.
    
    Args:
        matrix1 (dict): First sparse matrix represented as {row_index: row_vector}
        matrix2 (dict): Second sparse matrix represented as {row_index: row_vector}
    
    Returns:
        dict: Resulting sparse matrix after multiplication
    
    Raises:
        ValueError: If matrices cannot be multiplied due to dimension mismatch
    """
    # Validate matrix compatibility
    if not matrix1 or not matrix2:
        return {}
    
    # Validate column-row compatibility
    m1_cols = len(next(iter(matrix1.values()), []))
    m2_rows = len(matrix2)
    
    if m1_cols != m2_rows:
        raise ValueError(f"Matrix dimensions incompatible: {m1_cols} != {m2_rows}")
    
    # Compute result matrix
    result = {}
    
    for i, row1 in matrix1.items():
        result_row = {}
        for j, col_val in enumerate(row1):
            if col_val == 0:
                continue
            
            # Multiply row value with corresponding column of matrix2
            for k, val2 in matrix2[j].items():
                result_row[k] = result_row.get(k, 0) + col_val * val2
        
        # Only add non-zero rows to result
        if result_row:
            result[i] = result_row
    
    return result