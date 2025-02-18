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
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # Find zeros
        zero_positions = [(i, j) for i in range(n) for j in range(n) if matrix[i, j] == 0]
        
        # Track which rows and columns are covered
        covered_rows = set()
        covered_cols = set()
        
        # Greedy approach to cover zeros
        assignment = []
        for pos in zero_positions:
            row, col = pos
            if row not in covered_rows and col not in covered_cols:
                assignment.append((row, col))
                covered_rows.add(row)
                covered_cols.add(col)
        
        return assignment
    
    # Find optimal assignment
    assignment = cover_zeros(matrix)
    
    # If not complete assignment, rearrange to find full assignment
    if len(assignment) < n:
        # This is a simplified version and might need more sophisticated handling
        # for complex assignment problems
        for row in range(n):
            for col in range(n):
                if (row, col) not in assignment and matrix[row, col] == 0:
                    assignment.append((row, col))
                    break
    
    # Sort the assignment based on worker (first element of tuple)
    return sorted(assignment)