def search_matrix(matrix, target):
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of unique integers 
        target (int): The integer to search for
    
    Returns:
        bool: True if target is found, False otherwise
    
    Raises:
        ValueError: If the matrix is empty or not a valid 2D list
    """
    # Check for empty matrix
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Check matrix is rectangular 
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Optimized search leveraging sorted property (if exists)
    for row in matrix:
        # Validate row length
        if len(row) != cols:
            raise ValueError("Matrix must be rectangular")
        
        # Check if target could be in this row (if matrix is sorted)
        if row and (target >= row[0] and target <= row[-1]):
            # Linear search within the row
            if target in row:
                return True
    
    return False