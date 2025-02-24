def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for a target integer in a matrix of unique integers.

    This function efficiently searches a 2D matrix of unique integers to determine
    if the target is present. It uses a binary search approach to achieve 
    O(log(T*R)) time complexity, where T is the number of rows and R is the 
    number of columns.

    Args:
        matrix (list[list[int]]): A 2D matrix of unique integers.
        target (int): The integer to search for in the matrix.

    Returns:
        bool: True if the target is found in the matrix, False otherwise.

    Raises:
        ValueError: If the input matrix is empty or not a valid 2D matrix.
    
    Time Complexity: O(log(T*R))
    Space Complexity: O(1)
    """
    # Check for invalid matrix input
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Get matrix dimensions
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Treat matrix as a flattened sorted array
    left, right = 0, rows * cols - 1
    
    while left <= right:
        # Calculate mid point
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix coordinates
        row = mid // cols
        col = mid % cols
        
        # Get the value at current position
        current_val = matrix[row][col]
        
        # Compare and adjust search space
        if current_val == target:
            return True
        elif current_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Target not found
    return False