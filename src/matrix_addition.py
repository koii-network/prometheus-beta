from typing import List, Union

def add_matrices(matrix1: List[List[Union[int, float]]], 
                 matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Add two matrices by adding corresponding elements.
    
    Args:
        matrix1 (List[List[Union[int, float]]]): First input matrix
        matrix2 (List[List[Union[int, float]]]): Second input matrix
    
    Returns:
        List[List[Union[int, float]]]: Resulting matrix after addition
    
    Raises:
        ValueError: If matrices are not compatible for addition
        TypeError: If input is not a valid matrix
    """
    # Check if inputs are lists
    if not isinstance(matrix1, list) or not isinstance(matrix2, list):
        raise TypeError("Inputs must be lists of lists")
    
    # Check if matrices are empty
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")
    
    # Check matrix1 rows have consistent length
    if any(not isinstance(row, list) for row in matrix1):
        raise TypeError("Matrix1 must be a list of lists")
    row_lengths1 = set(len(row) for row in matrix1)
    if len(row_lengths1) > 1:
        raise ValueError("All rows in matrix1 must have the same length")
    
    # Check matrix2 rows have consistent length
    if any(not isinstance(row, list) for row in matrix2):
        raise TypeError("Matrix2 must be a list of lists")
    row_lengths2 = set(len(row) for row in matrix2)
    if len(row_lengths2) > 1:
        raise ValueError("All rows in matrix2 must have the same length")
    
    # Check matrix dimensions match
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    
    # Check for numeric elements
    for row in matrix1 + matrix2:
        if any(not isinstance(el, (int, float)) for el in row):
            raise TypeError("Matrix elements must be numeric (int or float)")
    
    # Perform matrix addition
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]