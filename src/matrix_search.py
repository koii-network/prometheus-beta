def search_matrix(matrix, target):
    """
    Search for a target value in a matrix with specific search constraints.
    
    The matrix has the following properties:
    - Each row is sorted in ascending order from left to right
    - The first integer of each row is greater than the last integer of the previous row
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The value to search for in the matrix
    
    Returns:
        bool: True if the target is found, False otherwise
    
    Time Complexity: O(log(m*n)) where m is the number of rows and n is the number of columns
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer
        ValueError: If the matrix is empty or contains non-integer elements
    """
    # Input validation
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a list of lists")
    
    # Short-circuit for empty matrix
    if not matrix:
        return False
    
    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check if matrix is empty or contains empty rows
    if not matrix[0]:
        return False
    
    # Validate matrix structure and elements
    for row in matrix:
        if not all(isinstance(x, int) for x in row):
            raise ValueError("Matrix must contain only integers")
        if not all(row[i] <= row[i+1] for i in range(len(row)-1)):
            raise ValueError("Rows must be sorted in ascending order")
    
    # Binary search across the entire matrix
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False