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
        bool: True if the target is found in the matrix, False otherwise
    
    Time complexity: O(log(m*n)), where m is the number of rows and n is the number of columns
    Space complexity: O(1)
    """
    # Handle empty matrix
    if not matrix or not matrix[0]:
        return False
    
    # Get matrix dimensions
    m, n = len(matrix), len(matrix[0])
    
    # Binary search on the entire matrix treated as a sorted 1D array
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix indices
        row = mid // n
        col = mid % n
        
        # Get the value at the current index
        current_value = matrix[row][col]
        
        # Compare with target and adjust search space
        if current_value == target:
            return True
        elif current_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False