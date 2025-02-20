def search_matrix(matrix, target):
    """
    Search for a target value in a matrix with specific search constraints.
    
    The matrix has the following properties:
    - Each row is sorted in ascending order
    - The first integer of each row is greater than the last integer of the previous row
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The value to search for
    
    Returns:
        bool: True if target is found in the matrix, False otherwise
    
    Time Complexity: O(log(m*n)) where m is number of rows, n is number of columns
    Space Complexity: O(1)
    """
    # Handle empty matrix
    if not matrix or not matrix[0]:
        return False
    
    # Get matrix dimensions
    rows, cols = len(matrix), len(matrix[0])
    
    # Binary search on the flattened matrix
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert mid to row and column indices
        row = mid // cols
        col = mid % cols
        
        # Get the current value
        current = matrix[row][col]
        
        # Compare with target
        if current == target:
            return True
        elif current < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False