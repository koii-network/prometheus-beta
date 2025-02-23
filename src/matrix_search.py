def search_matrix(matrix, target):
    """
    Search for a target value in a matrix with sorted inner lists.
    
    Args:
        matrix (List[List[int]]): 2D matrix where inner lists are sorted in ascending order
        target (int): The value to search for in the matrix
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    
    Time Complexity: O(m log n), where m is the number of rows and n is the length of each row
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list or target is not an integer
        ValueError: If the matrix is empty or contains non-integer elements
    """
    # Input validation
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a list of lists")
    
    if not matrix or not matrix[0]:
        return False
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check matrix validity
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("Each row must be a list")
        
        if not all(isinstance(x, int) for x in row):
            raise ValueError("Matrix must contain only integers")
    
    # Binary search in sorted rows
    for row in matrix:
        left, right = 0, len(row) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = row[mid]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
    
    return False