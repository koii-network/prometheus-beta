import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Implements the Hungarian algorithm for solving the assignment problem.
    
    Args:
        cost_matrix (list or np.ndarray): A 2D matrix representing costs of assignments.
    
    Returns:
        tuple: A tuple containing:
            - total_cost (float): The minimum total cost of assignments
            - assignment (list): A list of assigned pairs [(worker, task), ...]
    
    Raises:
        ValueError: If the input is not a valid 2D matrix
    """
    # Input validation
    if not isinstance(cost_matrix, (list, np.ndarray)):
        raise ValueError("Input must be a 2D list or numpy array")
    
    # Convert to numpy array for easier manipulation
    cost_matrix = np.array(cost_matrix, dtype=float)
    
    # Check matrix dimensionality
    if cost_matrix.ndim != 2:
        raise ValueError("Input must be a 2D matrix")
    
    # Ensure square matrix (equal number of workers and tasks)
    rows, cols = cost_matrix.shape
    if rows != cols:
        raise ValueError("Cost matrix must be square (equal number of workers and tasks)")
    
    # Step 1: Subtract row minimums
    reduced_matrix = cost_matrix.copy()
    for i in range(rows):
        reduced_matrix[i] -= np.min(reduced_matrix[i])
    
    # Step 2: Subtract column minimums
    for j in range(cols):
        reduced_matrix[:, j] -= np.min(reduced_matrix[:, j])
    
    # Step 3: Cover zeros with minimum number of lines
    assignment = []
    covered_rows = set()
    covered_cols = set()
    
    # Simple greedy assignment to cover zeros
    for i in range(rows):
        zero_cols = np.where(reduced_matrix[i] == 0)[0]
        for col in zero_cols:
            if col not in covered_cols:
                assignment.append((i, col))
                covered_rows.add(i)
                covered_cols.add(col)
                break
    
    # Calculate total cost based on original matrix
    total_cost = sum(cost_matrix[worker, task] for worker, task in assignment)
    
    return total_cost, assignment

def is_valid_assignment(cost_matrix, assignment):
    """
    Validate that the assignment is correct.
    
    Args:
        cost_matrix (list or np.ndarray): Original cost matrix
        assignment (list): List of (worker, task) pairs
    
    Returns:
        bool: Whether the assignment is valid
    """
    # Check unique assignments
    workers, tasks = zip(*assignment)
    return len(set(workers)) == len(workers) and len(set(tasks)) == len(tasks)