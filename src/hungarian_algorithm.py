import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solves the Assignment Problem using the Hungarian Algorithm.
    
    Args:
        cost_matrix (list of lists or np.ndarray): A rectangular matrix of costs 
        where each cell represents the cost of assigning a worker to a job.
    
    Returns:
        tuple: A tuple containing:
            - total_cost (float): The minimum total cost of the assignment
            - assignment (list): A list of (worker, job) pairs representing the optimal assignment
    
    Raises:
        ValueError: If the input is not a valid cost matrix
    """
    # Convert input to numpy array for easier manipulation
    if not isinstance(cost_matrix, np.ndarray):
        cost_matrix = np.array(cost_matrix)
    
    # Validate input
    if cost_matrix.ndim != 2:
        raise ValueError("Cost matrix must be a 2D array")
    
    # Create a working copy of the cost matrix
    matrix = cost_matrix.copy().astype(float)
    
    # Step 1: Subtract row minima from each row
    for i in range(matrix.shape[0]):
        matrix[i] -= matrix[i].min()
    
    # Step 2: Subtract column minima from each column
    for j in range(matrix.shape[1]):
        matrix[:, j] -= matrix[:, j].min()
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # Find rows and columns with zeros
        rows, cols = matrix.shape
        row_cover = [False] * rows
        col_cover = [False] * cols
        
        # Greedy coverage of zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] == 0 and not row_cover[i] and not col_cover[j]:
                    row_cover[i] = True
                    col_cover[j] = True
        
        return row_cover, col_cover
    
    # Step 4: Find optimal assignment
    def find_assignment(matrix):
        rows, cols = matrix.shape
        assignment = []
        used_rows = set()
        used_cols = set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] == 0 and i not in used_rows and j not in used_cols:
                    assignment.append((i, j))
                    used_rows.add(i)
                    used_cols.add(j)
                    break
        
        return assignment
    
    # Perform assignment
    row_cover, col_cover = cover_zeros(matrix)
    assignment = find_assignment(matrix)
    
    # Calculate total cost
    total_cost = sum(cost_matrix[worker, job] for worker, job in assignment)
    
    return int(total_cost), assignment