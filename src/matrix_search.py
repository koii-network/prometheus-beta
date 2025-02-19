def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (list[list[int]]): A 2D matrix of unique integers
        target (int): The integer to search for
    
    Returns:
        bool: True if target is in the matrix, False otherwise
    
    Raises:
        ValueError: If the matrix is empty or contains non-unique elements
    """
    # Check for empty matrix
    if not matrix or not matrix[0]:
        return False
    
    # Check for matrix integrity (non-empty rows)
    if any(not row for row in matrix):
        return False
    
    # Validate unique elements
    all_elements = [num for row in matrix for num in row]
    if len(set(all_elements)) != len(all_elements):
        raise ValueError("Matrix must contain unique integers")
    
    # Perform matrix search
    for row in matrix:
        if target in row:
            return True
    
    return False