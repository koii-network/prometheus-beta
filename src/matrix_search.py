def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for a target integer in an M x N matrix.
    
    The matrix is assumed to be a 2D list where each row is sorted in ascending order,
    and the first integer of each row is greater than the last integer of the previous row.
    
    Args:
        matrix (list[list[int]]): A 2D list of integers
        target (int): The integer to search for
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    
    Time Complexity: O(log(m*n)) - binary search approach
    Space Complexity: O(1) - constant extra space
    
    Raises:
        TypeError: If matrix is not a list or contains non-integer elements
        ValueError: If matrix is empty or contains empty rows
    """
    # Validate input matrix
    if not matrix or not matrix[0]:
        return False
    
    # Validate matrix structure and elements
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a 2D list")
    
    # Flatten matrix dimensions
    m, n = len(matrix), len(matrix[0])
    
    # Binary search on flattened matrix
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix coordinates
        row = mid // n
        col = mid % n
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False