def reverse_matrix_elements(matrix):
    """
    Reverses each element in the input matrix.
    
    Args:
    matrix (List[List[int]]): A square matrix of integers between 0 and 9.
    
    Returns:
    List[List[int]]: A new matrix with each element reversed.
    
    Raises:
    ValueError: If the input is not a valid square matrix or contains elements outside [0,9].
    """
    # Validate input matrix
    if not matrix or not isinstance(matrix, list):
        raise ValueError("Input must be a non-empty list")
    
    # Check if matrix is square
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square (NxN)")
    
    # Validate matrix contents
    for row in matrix:
        if not all(isinstance(x, int) and 0 <= x <= 9 for x in row):
            raise ValueError("Matrix must contain integers between 0 and 9")
    
    # Create new matrix with reversed elements
    def reverse_number(num):
        # Handle single-digit and multi-digit numbers
        return int(str(num)[::-1])
    
    return [[reverse_number(elem) for elem in row] for row in matrix]