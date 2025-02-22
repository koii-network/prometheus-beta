def search_matrix(matrix, target):
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of unique integers
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target is found, False otherwise
    
    Raises:
        ValueError: If the input matrix is empty or not a valid 2D list
    """
    # Check if matrix is empty or not a valid 2D list
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Get matrix dimensions
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Perform binary search on the flattened matrix
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert mid to 2D coordinates
        row = mid // cols
        col = mid % cols
        
        # Get the value at the current position
        current_value = matrix[row][col]
        
        # Compare and adjust search space
        if current_value == target:
            return True
        elif current_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False