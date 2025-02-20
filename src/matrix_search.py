def search_matrix(matrix, target, search_constraints=None):
    """
    Search for a target value in a matrix with optional search constraints.
    
    Args:
    - matrix (List[List[int]]): 2D matrix to search
    - target (int): Value to find
    - search_constraints (dict, optional): Constraints for the search
      Possible constraints:
      - 'direction': 'row', 'column', or None (default, search entire matrix)
      - 'start_row' (int): Starting row index for search
      - 'end_row' (int): Ending row index for search
      - 'start_col' (int): Starting column index for search
      - 'end_col' (int): Ending column index for search
    
    Returns:
    - Tuple[bool, List[int]]: (found, [row, col]) or (False, [])
    
    Raises:
    - ValueError: If search constraints are invalid
    """
    # Validate input matrix
    if not matrix or not matrix[0]:
        return False, []
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Process and validate search constraints
    if search_constraints is None:
        search_constraints = {}
    
    start_row = search_constraints.get('start_row', 0)
    end_row = search_constraints.get('end_row', rows - 1)
    start_col = search_constraints.get('start_col', 0)
    end_col = search_constraints.get('end_col', cols - 1)
    direction = search_constraints.get('direction')
    
    # Validate constraint ranges
    if (start_row < 0 or end_row >= rows or start_col < 0 or end_col >= cols or
        start_row > end_row or start_col > end_col):
        raise ValueError("Invalid search constraints")
    
    # Search based on direction
    if direction == 'row':
        # Search specific rows
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                if matrix[row][col] == target:
                    return True, [row, col]
    
    elif direction == 'column':
        # Search specific columns
        for col in range(start_col, end_col + 1):
            for row in range(start_row, end_row + 1):
                if matrix[row][col] == target:
                    return True, [row, col]
    
    else:
        # Default: search entire specified matrix region
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                if matrix[row][col] == target:
                    return True, [row, col]
    
    # Target not found
    return False, []