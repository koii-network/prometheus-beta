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
        # Backtracking with tracking used workers and tasks
        def backtrack(current_assignment):
            # If assignment is complete
            if len(current_assignment) == n:
                return current_assignment
            
            # Find unassigned workers
            assigned_workers = set(w for w, _ in current_assignment)
            unassigned_workers = [w for w in range(n) if w not in assigned_workers]
            
            for worker in unassigned_workers:
                for task in range(n):
                    # Check if task is already assigned
                    if any(t == task for _, t in current_assignment):
                        continue
                    
                    # If zero exists at this position, try this assignment
                    if matrix[worker, task] == 0:
                        new_assignment = current_assignment + [(worker, task)]
                        
                        # Recursively try to complete assignment
                        result = backtrack(new_assignment)
                        if result:
                            return result
            
            # No valid assignment found
            return None
        
        # Start with empty assignment
        return backtrack([])
    
    # Find optimal assignment
    assignment = find_optimal_assignment(matrix)
    
    # If no assignment found, raise an error
    if not assignment:
        raise ValueError("No valid assignment could be found")
    
    # Sort the assignment based on worker (first element of tuple)
    return sorted(assignment)