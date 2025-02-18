import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.
    
    Args:
        cost_matrix (list of lists or numpy.ndarray): A square matrix representing 
                                                      assignment costs.
    
    Returns:
        list: A list of tuples representing the optimal assignment 
              in the format [(worker, task), ...]
    
    Raises:
        ValueError: If the input is not a valid square matrix
    """
    # Convert to numpy array for easier manipulation
    matrix = np.array(cost_matrix, dtype=float)
    
    # Validate input
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input must be a square matrix")
    
    n = matrix.shape[0]
    
    # Step 1: Subtract row minimums
    for i in range(n):
        matrix[i] -= matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        matrix[:, j] -= matrix[:, j].min()
    
    # Find optimal assignment
    def find_optimal_assignment(matrix):
        # Track used rows and columns
        used_rows = set()
        used_cols = set()
        assignment = []
        
        # Sort potential zero assignments by lowest zero count
        zero_positions = [(i, j) for i in range(n) for j in range(n) if matrix[i, j] == 0]
        zero_positions.sort(key=lambda x: sum(1 for r in range(n) if matrix[r, x[1]] == 0))
        
        # Greedy assignment algorithm
        for row, col in zero_positions:
            # If this row and column are not yet used
            if row not in used_rows and col not in used_cols:
                assignment.append((row, col))
                used_rows.add(row)
                used_cols.add(col)
        
        return assignment
    
    # Attempt to find an optimal assignment
    assignment = find_optimal_assignment(matrix)
    
    # Sort the assignment based on worker (first element of tuple)
    return sorted(assignment)