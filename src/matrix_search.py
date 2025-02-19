def search_matrix(matrix, target):
    """
    Search for a target integer in a 2D matrix where:
    1. Inner lists are sorted in ascending order
    2. Rows are not necessarily sorted
    
    Args:
        matrix (List[List[int]]): 2D matrix of integers
        target (int): Target integer to find
    
    Returns:
        bool: True if target exists in matrix, False otherwise
    
    Time Complexity: O(m log n), where m is number of rows, n is number of columns
    Space Complexity: O(1)
    """
    if not matrix or not matrix[0]:
        return False
    
    # For each row, perform binary search 
    for row in matrix:
        # Check if target could be in this row
        if row and (target >= row[0] and target <= row[-1]):
            # Perform binary search on the row
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