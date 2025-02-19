def search_matrix(matrix, target):
    """
    Search for a target integer in an M x N matrix.
    
    The matrix is assumed to be sorted in ascending order from left to right and top to bottom.
    This implementation uses an efficient O(log(m*n)) search approach.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The integer to search for
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    """
    # Handle empty matrix
    if not matrix or not matrix[0]:
        return False
    
    # Get matrix dimensions
    m, n = len(matrix), len(matrix[0])
    
    # Binary search across the entire matrix
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix indices
        row = mid // n
        col = mid % n
        
        # Get the value at the mid point
        mid_value = matrix[row][col]
        
        # Compare mid value with target
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False