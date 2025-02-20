def search_matrix(matrix, target, constraints=None):
    """
    Search for a target value in a matrix with optional search constraints.
    
    Args:
        matrix (List[List[int]]): 2D matrix to search
        target (int): Value to find
        constraints (dict, optional): Additional search constraints
            - 'strictly_increasing' (bool): Enforce strictly increasing order
            - 'row_wise' (bool): Search row-wise first
            - 'max_iterations' (int): Maximum number of iterations allowed
    
    Returns:
        tuple: (found, position)
            - found (bool): Whether the target was found
            - position (tuple): (row, col) of the target, or (-1, -1) if not found
    """
    # Input validation
    if not matrix or not matrix[0]:
        return False, (-1, -1)
    
    # Extract constraints with default values
    strictly_increasing = constraints.get('strictly_increasing', False) if constraints else False
    row_wise = constraints.get('row_wise', True) if constraints else True
    max_iterations = constraints.get('max_iterations', len(matrix) * len(matrix[0])) if constraints else len(matrix) * len(matrix[0])
    
    # Validate strictly increasing constraint if specified
    if strictly_increasing:
        def is_strictly_increasing(arr):
            return all(arr[i] < arr[i+1] for i in range(len(arr)-1))
        
        # Check row-wise increasing
        for row in matrix:
            if not is_strictly_increasing(row):
                return False, (-1, -1)
        
        # Check column-wise increasing
        for col in range(len(matrix[0])):
            column = [matrix[row][col] for row in range(len(matrix))]
            if not is_strictly_increasing(column):
                return False, (-1, -1)
    
    # Perform search
    iterations = 0
    if row_wise:
        # Row-wise search
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                iterations += 1
                if iterations > max_iterations:
                    return False, (-1, -1)
                
                if matrix[row][col] == target:
                    return True, (row, col)
    else:
        # Column-wise search
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                iterations += 1
                if iterations > max_iterations:
                    return False, (-1, -1)
                
                if matrix[row][col] == target:
                    return True, (row, col)
    
    return False, (-1, -1)