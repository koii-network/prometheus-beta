def search_matrix(matrix, target):
    """
    Search for a target integer in an M x N matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The target integer to find
    
    Returns:
        bool: True if target exists in matrix, False otherwise
    
    Time Complexity: O(m+n), where m is number of rows, n is number of columns
    Space Complexity: O(1)
    """
    # Handle empty matrix
    if not matrix or not matrix[0]:
        return False
    
    # Get matrix dimensions
    rows, cols = len(matrix), len(matrix[0])
    
    # Start from top-right corner
    row, col = 0, cols - 1
    
    while row < rows and col >= 0:
        current = matrix[row][col]
        
        # Target found
        if current == target:
            return True
        
        # If current is larger, move left
        if current > target:
            col -= 1
        
        # If current is smaller, move down
        else:
            row += 1
    
    return False