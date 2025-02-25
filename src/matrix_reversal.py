def reverse_matrix_elements(matrix):
    """
    Reverse the digits of each element in a square matrix.

    Args:
        matrix (List[List[int]]): A square matrix of integers between 0 and 9.

    Returns:
        List[List[int]]: A new matrix with each element's digits reversed.

    Raises:
        ValueError: If the matrix is not square or contains invalid elements.
    """
    # Validate input matrix
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")

    # Check if matrix is square
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square")

    # Check matrix size constraints
    if not (1 <= n <= 1000):
        raise ValueError("Matrix size must be between 1 and 1000")

    # Validate matrix elements
    for row in matrix:
        if any(not (0 <= elem <= 9) for elem in row):
            raise ValueError("Matrix elements must be integers between 0 and 9")

    # Create a new matrix with reversed elements
    reversed_matrix = []
    for row in matrix:
        reversed_row = [int(str(elem)[::-1]) for elem in row]
        reversed_matrix.append(reversed_row)

    return reversed_matrix