def search_matrix(matrix, target, constraints=None):
    """
    Search for a target value in a matrix with optional search constraints.
    
    Args:
        matrix (List[List[int]]): 2D matrix to search
        target (int): Value to find
        constraints (dict, optional): Additional search constraints
    
    Returns:
        tuple: (row_index, col_index) if found, else (-1, -1)
    
    Constraints:
    - 'sorted_rows': If True, assumes each row is sorted in ascending order
    - 'sorted_cols': If True, assumes each column is sorted in ascending order
    - 'row_range': Limit search to specific row range (start_row, end_row)
    - 'col_range': Limit search to specific column range (start_col, end_col)
    """
    if not matrix or not matrix[0]:
        return -1, -1
    
    # Default constraints
    if constraints is None:
        constraints = {}
    
    # Extract constraints
    sorted_rows = constraints.get('sorted_rows', False)
    sorted_cols = constraints.get('sorted_cols', False)
    row_range = constraints.get('row_range', (0, len(matrix)))
    col_range = constraints.get('col_range', (0, len(matrix[0])))
    
    start_row, end_row = row_range
    start_col, end_col = col_range
    
    # Boundary checks
    if start_row < 0 or end_row > len(matrix) or start_col < 0 or end_col > len(matrix[0]):
        return -1, -1
    
    # Binary search for sorted matrix
    if sorted_rows and sorted_cols:
        return _binary_search_sorted_matrix(matrix, target, start_row, end_row, start_col, end_col)
    
    # Linear search for unsorted or partially sorted matrix
    return _linear_search_matrix(matrix, target, start_row, end_row, start_col, end_col)

def _linear_search_matrix(matrix, target, start_row, end_row, start_col, end_col):
    """
    Perform linear search through the specified matrix region.
    
    Args:
        matrix (List[List[int]]): 2D matrix to search
        target (int): Value to find
        start_row, end_row, start_col, end_col (int): Search region boundaries
    
    Returns:
        tuple: (row_index, col_index) if found, else (-1, -1)
    """
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            if matrix[row][col] == target:
                return row, col
    return -1, -1

def _binary_search_sorted_matrix(matrix, target, start_row, end_row, start_col, end_col):
    """
    Perform binary search in a sorted matrix.
    
    Args:
        matrix (List[List[int]]): Sorted 2D matrix to search
        target (int): Value to find
        start_row, end_row, start_col, end_col (int): Search region boundaries
    
    Returns:
        tuple: (row_index, col_index) if found, else (-1, -1)
    """
    while start_row < end_row and start_col < end_col:
        # Find middle row and column
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        
        if matrix[mid_row][mid_col] == target:
            return mid_row, mid_col
        
        # Eliminate quadrants that cannot contain the target
        if matrix[mid_row][mid_col] < target:
            # Target is in lower right quadrant
            start_row = mid_row + 1
            start_col = mid_col + 1
        else:
            # Target is in upper left quadrant
            end_row = mid_row
            end_col = mid_col
    
    return -1, -1