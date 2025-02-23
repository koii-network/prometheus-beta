def search_sorted_matrix(matrix, target):
    """
    Search for a target integer in a 2D matrix with sorted inner lists.
    
    Args:
        matrix (List[List[int]]): A 2D matrix where inner lists are sorted in ascending order.
        target (int): The integer to search for in the matrix.
    
    Returns:
        bool: True if the target is found in the matrix, False otherwise.
    
    Time Complexity: O(m * log(n)), where m is the number of rows and n is the number of columns
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer
    """
    # Validate input
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Handle empty matrix
    if not matrix or not matrix[0]:
        return False
    
    # Search each row using binary search
    for row in matrix:
        # Ensure row is sorted in ascending order
        if not all(row[i] <= row[i+1] for i in range(len(row)-1)):
            raise ValueError("Inner lists must be sorted in ascending order")
        
        # Binary search within the row
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
    # Target not found
    return False