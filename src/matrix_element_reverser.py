def reverse_matrix_elements(matrix):
    """
    Reverses each element of the input matrix.
    
    Args:
        matrix (List[List[int]]): A square matrix of integers in range [0, 9]
    
    Returns:
        List[List[int]]: A new matrix with each element reversed
    
    Raises:
        ValueError: If matrix is empty, not square, or contains elements outside [0, 9]
    """
    # Input validation
    if not matrix or len(matrix) == 0:
        raise ValueError("Matrix cannot be empty")
    
    # Check if matrix is square
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square")
    
    # Check matrix size constraints
    if n < 1 or n > 1000:
        raise ValueError("Matrix size must be between 1 and 1000")
    
    # Validate matrix elements
    for row in matrix:
        if any(not (0 <= num <= 9) for num in row):
            raise ValueError("Matrix elements must be in range [0, 9]")
    
    # Create a new matrix with reversed elements
    return [[int(str(num)[::-1]) for num in row] for row in matrix]