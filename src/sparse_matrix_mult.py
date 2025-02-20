def sparse_matrix_multiply(matrix1, matrix2):
    """
    Perform sparse matrix multiplication using dictionary representation.
    
    :param matrix1: First sparse matrix (dict with row indices as keys, row vectors as values)
    :param matrix2: Second sparse matrix (dict with row indices as keys, row vectors as values)
    :return: Resulting sparse matrix after multiplication
    """
    # Check if multiplication is possible
    if not matrix1 or not matrix2:
        return {}
    
    # Check column and row compatibility
    result = {}
    
    # Iterate through rows of first matrix
    for i, row1 in matrix1.items():
        result_row = {}
        
        # Iterate through columns of second matrix
        for j, val1 in row1.items():
            # Check if this column exists in matrix2
            if j in matrix2:
                # Multiply row values
                for k, val2 in matrix2[j].items():
                    # Compute dot product for this cell
                    prod = val1 * val2
                    
                    # Update result matrix cell
                    if prod != 0:
                        # Only store non-zero values
                        if i not in result:
                            result[i] = {}
                        result[i][k] = result[i].get(k, 0) + prod
        
        # Remove rows with no non-zero elements
        if i in result and not result[i]:
            del result[i]
    
    return result