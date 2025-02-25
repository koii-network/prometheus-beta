"""
Matrix operations module providing functionality for matrix addition.
"""
from typing import List, Union


def add_matrices(matrix1: List[List[Union[int, float]]], 
                 matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Add two matrices by adding corresponding elements.

    Args:
        matrix1 (List[List[Union[int, float]]]): First input matrix
        matrix2 (List[List[Union[int, float]]]): Second input matrix

    Returns:
        List[List[Union[int, float]]]: Resultant matrix after addition

    Raises:
        ValueError: If matrices have incompatible dimensions
        TypeError: If input is not a valid matrix (list of lists with numeric elements)
    """
    # Validate input is a matrix (list of lists)
    if not (isinstance(matrix1, list) and isinstance(matrix2, list)):
        raise TypeError("Inputs must be lists")
    
    # Check if matrices are empty
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")
    
    # Validate matrices have consistent row lengths
    if any(not isinstance(row, list) for row in matrix1 + matrix2):
        raise TypeError("Each row must be a list")
    
    # Check row lengths are consistent within each matrix
    if any(len(row) != len(matrix1[0]) for row in matrix1):
        raise ValueError("Rows in first matrix must have equal length")
    if any(len(row) != len(matrix2[0]) for row in matrix2):
        raise ValueError("Rows in second matrix must have equal length")
    
    # Check matrices have same dimensions
    if (len(matrix1) != len(matrix2)) or (len(matrix1[0]) != len(matrix2[0])):
        raise ValueError("Matrices must have the same dimensions")
    
    # Validate numeric types
    for row in matrix1 + matrix2:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("Matrix elements must be numeric")
    
    # Perform matrix addition
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] 
        for i in range(len(matrix1))
    ]