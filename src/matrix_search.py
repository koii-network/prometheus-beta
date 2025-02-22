def search_matrix(matrix, target):
    """
    Search for a target integer in a 2D matrix with sorted inner lists.
    
    Args:
        matrix (List[List[int]]): 2D matrix where inner lists are sorted
        target (int): Target integer to find
    
    Returns:
        bool: True if target exists in matrix, False otherwise
    
    Time Complexity: O(m log n), where m is number of rows and n is number of columns
    Space Complexity: O(1)
    """
    if not matrix or not matrix[0]:
        return False
    
    # Iterate through rows
    for row in matrix:
        # Binary search within each row
        left, right = 0, len(row) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
    return False