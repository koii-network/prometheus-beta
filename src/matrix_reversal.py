def reverse_matrix_elements(matrix):
    """
    Reverse each element in the given matrix.
    
    :param matrix: A list of lists representing an N x N matrix of integers
    :return: A new matrix with each element reversed
    :raises ValueError: If the matrix is not square or contains elements outside [0, 9]
    """
    # Validate matrix is square
    if not matrix or len(matrix) == 0 or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Matrix must be a square, non-empty matrix")
    
    # Validate matrix size
    n = len(matrix)
    if n < 1 or n > 1000:
        raise ValueError("Matrix size must be between 1 and 1000")
    
    # Validate matrix elements
    for row in matrix:
        if not all(isinstance(elem, int) and 0 <= elem <= 9 for elem in row):
            raise ValueError("Matrix elements must be integers in the range [0, 9]")
    
    # Create a new matrix with reversed elements
    reversed_matrix = []
    for row in matrix:
        reversed_row = [int(str(elem)[::-1]) for elem in row]
        reversed_matrix.append(reversed_row)
    
    return reversed_matrix