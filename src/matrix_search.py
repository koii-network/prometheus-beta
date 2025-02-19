def search_matrix(matrix, target):
    """
    Search for a target integer in an M x N matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The integer to search for
    
    Returns:
        bool: True if target exists in the matrix, False otherwise
    
    Time Complexity: O(log(m*n))
    Space Complexity: O(1)
    
    Assumptions:
    - Matrix may be sorted (either row-wise or column-wise)
    - Empty matrix returns False
    """
    # Handle empty matrix case
    if not matrix or not matrix[0]:
        return False
    
    # Get matrix dimensions
    m, n = len(matrix), len(matrix[0])
    
    # Treat matrix as a flattened sorted array
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix indices
        row = mid // n
        col = mid % n
        
        # Compare mid element with target
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False