from typing import List, Optional, Tuple

def find_matrix_coordinates(matrix: List[List[int]], target: int) -> Optional[Tuple[int, int]]:
    """
    Find the coordinates of a target value in a 2D matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers to search through.
        target (int): The value to find in the matrix.
    
    Returns:
        Optional[Tuple[int, int]]: Coordinates (row, column) of the target value,
        or None if the target is not found.
    
    Raises:
        TypeError: If the input is not a valid 2D matrix or contains non-integer values.
        ValueError: If the matrix is empty.
    
    Time Complexity: O(m*n), where m is the number of rows and n is the number of columns
    Space Complexity: O(1) as we only use a constant amount of extra space
    
    Examples:
        >>> find_matrix_coordinates([[1,2,3],[4,5,6],[7,8,9]], 5)
        (1, 1)
        >>> find_matrix_coordinates([[1,2,3],[4,5,6],[7,8,9]], 10)
        None
    """
    # Validate input matrix
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Validate matrix structure and content
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a 2D list")
    
    # Check that all elements are integers
    try:
        matrix_copy = [[int(elem) for elem in row] for row in matrix]
    except (TypeError, ValueError):
        raise TypeError("Matrix must contain only integer values")
    
    # Ensure all rows have the same length
    if len(set(len(row) for row in matrix_copy)) > 1:
        raise ValueError("All rows in the matrix must have the same length")
    
    # Search through the matrix
    for row_idx, row in enumerate(matrix_copy):
        for col_idx, value in enumerate(row):
            if value == target:
                return (row_idx, col_idx)
    
    # Target not found
    return None