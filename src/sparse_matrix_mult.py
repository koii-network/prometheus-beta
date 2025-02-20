def sparse_matrix_multiply(matrix1, matrix2):
    """
    Perform sparse matrix multiplication using dictionary representation.
    
    :param matrix1: First sparse matrix (dict with row indices as keys, row vectors as values)
    :param matrix2: Second sparse matrix (dict with row indices as keys, row vectors as values)
    :return: Resulting sparse matrix after multiplication
    """
    # Validate input matrices
    if not isinstance(matrix1, dict) or not isinstance(matrix2, dict):
        raise TypeError("Inputs must be dictionaries representing sparse matrices")
    
    # Compute the result sparse matrix
    result = {}
    
    # Iterate through rows of first matrix
    for i, row1 in matrix1.items():
        result_row = {}
        
        # Iterate through columns of second matrix
        for j, val1 in row1.items():
            # Check if this column exists in the second matrix
            if j in matrix2:
                # Multiply row values from the corresponding matrix2 column
                for k, val2 in matrix2[j].items():
                    # Compute dot product
                    prod = val1 * val2
                    
                    # Add to result, creating row if not exists
                    if i not in result:
                        result[i] = {}
                    
                    # Update result, summing if key already exists
                    result[i][k] = result[i].get(k, 0) + prod
        
    return result