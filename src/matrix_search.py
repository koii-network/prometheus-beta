def search_matrix(matrix, target):
    """
    Search for a target value in a matrix with specific search constraints.
    
    The matrix has the following properties:
    - Each row is sorted in ascending order from left to right
    - The first integer of each row is greater than the last integer of the previous row
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The value to search for
    
    Returns:
        bool: True if the target is found in the matrix, False otherwise
    
    Time Complexity: O(log(m*n)) where m is number of rows and n is number of columns
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list of lists or if target is not an integer
        ValueError: If matrix is empty or contains non-integer elements
    """
    # Input validation
    if not matrix or not matrix[0]:
        return False
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    if not all(isinstance(num, int) for row in matrix for num in row):
        raise ValueError("Matrix must contain only integers")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Total number of rows and columns
    m = len(matrix)
    n = len(matrix[0])
    
    # Binary search across entire matrix
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix indices
        row = mid // n
        col = mid % n
        
        # Get the current value
        current = matrix[row][col]
        
        # Compare and adjust search space
        if current == target:
            return True
        elif current < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False