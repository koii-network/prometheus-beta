import numpy as np
from scipy.optimize import linear_sum_assignment

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
    
    # Use scipy's linear sum assignment method (which implements Hungarian algorithm)
    row_ind, col_ind = linear_sum_assignment(matrix)
    
    # Create assignment list of tuples
    assignment = list(zip(row_ind, col_ind))
    
    # Sort assignment based on worker (first element of tuple)
    return sorted(assignment)