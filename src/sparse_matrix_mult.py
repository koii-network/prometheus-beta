def sparse_matrix_multiply(matrix1, matrix2):
    """
    Perform sparse matrix multiplication using dictionary representation.
    
    :param matrix1: First sparse matrix (dict with row indices as keys, row vectors as values)
    :param matrix2: Second sparse matrix (dict with row indices as keys, row vectors as values)
    :return: Resulting sparse matrix after multiplication
    
    Raises:
    - ValueError if matrices cannot be multiplied (column count of first matrix 
      must match row count of second matrix)
    """
    # Validate matrix multiplication is possible
    if not matrix1 or not matrix2:
        return {}
    
    # Compute number of columns in matrix2
    matrix2_cols = max(max(col for col in row.keys()) for row in matrix2.values()) + 1 if matrix2 else 0
    
    # Resulting sparse matrix
    result = {}
    
    # Iterate through rows of first matrix
    for i, row1 in matrix1.items():
        # Create row for result matrix
        result_row = {}
        
        # Iterate through columns of second matrix
        for j in range(matrix2_cols):
            # Compute dot product
            dot_product = 0
            for k, val1 in row1.items():
                # Check if this column exists in matrix2
                if k in matrix2:
                    # Multiply and sum
                    dot_product += val1 * matrix2[k].get(j, 0)
            
            # Only add non-zero values to result
            if dot_product != 0:
                result_row[j] = dot_product
        
        # Only add non-empty rows to result
        if result_row:
            result[i] = result_row
    
    return result