import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm (Munkres algorithm).
    
    Args:
        cost_matrix (list of lists or numpy.ndarray): A square cost matrix 
        where cost_matrix[i][j] represents the cost of assigning worker i to task j.
    
    Returns:
        tuple: A tuple containing:
            - A list of assignments [(worker, task), ...]
            - The total minimum cost of the assignment
    
    Raises:
        ValueError: If the input is not a valid square matrix
    """
    # Convert input to numpy array for easier manipulation
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
    
    # Track covered rows and columns
    covered_rows = [False] * n
    covered_cols = [False] * n
    
    # Track assignments
    assignments = []
    
    # Mark zeros
    def mark_zeros():
        nonlocal assignments, covered_rows, covered_cols
        assignments = []
        covered_rows = [False] * n
        covered_cols = [False] * n
        
        # Find initial assignments
        for i in range(n):
            zero_cols = np.where((matrix[i] == 0) & (~np.array(covered_cols)))[0]
            if len(zero_cols) == 1:
                j = zero_cols[0]
                assignments.append((i, j))
                covered_rows[i] = True
                covered_cols[j] = True
    
    # Iterative steps to find optimal assignment
    def find_optimal_assignment():
        nonlocal matrix, covered_rows, covered_cols
        
        while len(assignments) < n:
            mark_zeros()
            
            # If we have a complete assignment, return
            if len(assignments) == n:
                break
            
            # Find the smallest uncovered element
            min_uncovered = float('inf')
            min_row, min_col = -1, -1
            
            for i in range(n):
                if not covered_rows[i]:
                    for j in range(n):
                        if not covered_cols[j]:
                            if matrix[i, j] < min_uncovered:
                                min_uncovered = matrix[i, j]
                                min_row, min_col = i, j
            
            # Adjust matrix
            matrix[covered_rows, :] += min_uncovered
            matrix[:, covered_cols] -= min_uncovered
            matrix[min_row, :] -= min_uncovered
            matrix[:, min_col] += min_uncovered
    
    # Run the algorithm
    find_optimal_assignment()
    
    # Calculate total cost
    total_cost = sum(cost_matrix[worker][task] for worker, task in assignments)
    
    return assignments, total_cost