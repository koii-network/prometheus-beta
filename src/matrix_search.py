def search_sorted_matrix(matrix, target):
    """
    Search for a target integer in a 2D matrix with sorted inner lists.
    
    Args:
        matrix (List[List[int]]): 2D matrix where inner lists are sorted 
                                  but rows are not necessarily sorted
        target (int): Integer to search for in the matrix
    
    Returns:
        bool: True if target is found, False otherwise
    
    Time Complexity: O(m * log(n)), where m is number of rows, n is number of columns
    Space Complexity: O(1)
    """
    # Handle empty matrix
    if not matrix or not matrix[0]:
        return False
    
    # Search through each row 
    for row in matrix:
        # If row is empty, skip
        if not row:
            continue
        
        # If target is out of row's range, skip row
        if target < row[0] or target > row[-1]:
            continue
        
        # Binary search in this row
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