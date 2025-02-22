import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.
    
    Args:
        cost_matrix (list of lists or numpy.ndarray): A square matrix representing 
                                                      assignment costs.
    
    Returns:
        list: Optimal assignment as a list of (row, column) pairs.
        float: Total minimum cost of the assignment.
    
    Raises:
        ValueError: If input is not a valid square cost matrix.
    """
    # Validate input
    if not isinstance(cost_matrix, (list, np.ndarray)):
        raise ValueError("Input must be a 2D list or numpy array")
    
    # Convert to numpy array for easier manipulation
    cost_matrix = np.array(cost_matrix, dtype=float)
    
    # Check matrix is square
    if cost_matrix.ndim != 2 or cost_matrix.shape[0] != cost_matrix.shape[1]:
        raise ValueError("Cost matrix must be a square matrix")
    
    n = cost_matrix.shape[0]
    
    # Step 1: Subtract row minimums
    row_min = cost_matrix.min(axis=1)
    cost_matrix = cost_matrix - row_min[:, np.newaxis]
    
    # Step 2: Subtract column minimums
    col_min = cost_matrix.min(axis=0)
    cost_matrix = cost_matrix - col_min
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # Greedy approach to cover zeros
        n = matrix.shape[0]
        row_cover = [False] * n
        col_cover = [False] * n
        
        # Find independent zeros
        assignment = []
        for row in range(n):
            for col in range(n):
                if matrix[row, col] == 0 and not row_cover[row] and not col_cover[col]:
                    assignment.append((row, col))
                    row_cover[row] = True
                    col_cover[col] = True
        
        # Count uncovered lines
        lines = sum(row_cover) + sum(col_cover)
        return assignment, lines
    
    # Step 4: Find optimal assignment
    assignment, lines = cover_zeros(cost_matrix)
    
    # If not perfect matching, adjust matrix
    while lines < n:
        # Find minimum uncovered value
        min_val = float('inf')
        for row in range(n):
            for col in range(n):
                if not row_cover[row] and not col_cover[col]:
                    min_val = min(min_val, cost_matrix[row, col])
        
        # Adjust matrix
        for row in range(n):
            for col in range(n):
                if not row_cover[row] and not col_cover[col]:
                    cost_matrix[row, col] -= min_val
                elif row_cover[row] and col_cover[col]:
                    cost_matrix[row, col] += min_val
        
        # Recheck assignment
        assignment, lines = cover_zeros(cost_matrix)
    
    # Calculate total cost
    total_cost = sum(row_min) + sum(col_min)
    total_cost += sum(cost_matrix[row, col] for row, col in assignment)
    
    return assignment, total_cost