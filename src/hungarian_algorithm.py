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
    matrix = np.array(cost_matrix, dtype=float).copy()
    
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
    
    # Find optimal assignment with backtracking
    def find_optimal_assignment(matrix):
        # Try all possible combinations
        def backtrack(assigned_rows, assigned_cols):
            if len(assigned_rows) == n:
                return assigned_rows
            
            for row in range(n):
                if row in assigned_rows:
                    continue
                
                for col in range(n):
                    if col in assigned_cols or matrix[row, col] != 0:
                        continue
                    
                    # Try this assignment
                    current_assigned = assigned_rows + [(row, col)]
                    current_cols = assigned_cols + [col]
                    
                    # Recursively attempt to complete assignment
                    full_assignment = backtrack(current_assigned, current_cols)
                    
                    if full_assignment:
                        return full_assignment
            
            return None
        
        # Attempt to find a full assignment
        return backtrack([], [])
    
    # Find optimal assignment
    assignment = find_optimal_assignment(matrix)
    
    # If no assignment found, raise an error
    if not assignment:
        raise ValueError("No valid assignment could be found")
    
    # Sort the assignment based on worker (first element of tuple)
    return sorted(assignment)