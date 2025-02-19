def search_matrix(matrix, target):
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of unique integers
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if target is found, False otherwise
    
    Raises:
        ValueError: If matrix is empty or not a valid 2D list
    """
    # Check for empty matrix
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Check matrix dimensions 
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Perform efficient search by treating matrix as a sorted 1D array
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix coordinates
        row = mid // cols
        col = mid % cols
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False