def reverse_matrix_elements(matrix):
    """
    Reverses each element in the input matrix.
    
    Args:
    matrix (List[List[int]]): A square matrix of integers between 0 and 9.
    
    Returns:
    List[List[int]]: A new matrix with each element reversed.
    
    Raises:
    ValueError: If the matrix is not square or contains elements outside [0, 9].
    """
    # Validate matrix is square
    if not matrix or len(matrix) == 0 or len(matrix) > 1000:
        raise ValueError("Matrix size must be between 1 and 1000")
    
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("Matrix must be square")
    
    # Validate matrix elements
    for row in matrix:
        if any(not (0 <= num <= 9) for num in row):
            raise ValueError("Matrix elements must be integers between 0 and 9")
    
    # Create new matrix with reversed elements
    return [[int(str(num)[::-1]) for num in row] for row in matrix]