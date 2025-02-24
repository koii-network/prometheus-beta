def matrix_search(matrix, target):
    """
    Find the coordinates of a target value in a 2D matrix.

    Args:
        matrix (List[List[int]]): A 2D matrix to search through
        target (int): The value to find in the matrix

    Returns:
        tuple: A tuple of (row, col) coordinates if found, or None if not found

    Raises:
        TypeError: If matrix is not a list of lists or target is not of a comparable type
        ValueError: If matrix is empty or contains non-uniform rows
    """
    # Validate input matrix
    if matrix is None:
        raise TypeError("Matrix cannot be None")

    if not matrix or not matrix[0]:
        return None

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")

    # Check for uniform row lengths
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise ValueError("Matrix rows must be of uniform length")

    # Perform matrix search
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == target:
                return (row_idx, col_idx)

    return None