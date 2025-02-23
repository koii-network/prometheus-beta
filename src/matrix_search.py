def search_matrix(matrix, target):
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of unique integers
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target is found in the matrix, False otherwise
    
    Raises:
        ValueError: If the input matrix is empty or invalid
    """
    # Check for empty matrix
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Get matrix dimensions
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Perform binary search leveraging the matrix's sorted property
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix coordinates
        mid_row = mid // cols
        mid_col = mid % cols
        mid_value = matrix[mid_row][mid_col]
        
        # Compare and adjust search space
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False