from typing import List, Optional, Tuple

def search_matrix(matrix: List[List[int]], target: int) -> Optional[Tuple[int, int]]:
    """
    Search for a target value in a matrix with specific search constraints.
    
    The matrix has the following properties:
    - Each row is sorted in ascending order
    - The first integer of each row is greater than the last integer of the previous row
    
    Args:
        matrix (List[List[int]]): 2D matrix of integers
        target (int): Value to search for
    
    Returns:
        Optional[Tuple[int, int]]: Tuple of (row, column) if target is found, 
                                   None if target is not in the matrix
    
    Raises:
        ValueError: If the input matrix is None or empty
    
    Time Complexity: O(log(m*n)), where m is number of rows, n is number of columns
    Space Complexity: O(1)
    """
    # Validate input
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be None or empty")
    
    # Get matrix dimensions
    rows, cols = len(matrix), len(matrix[0])
    
    # Binary search through the entire matrix as if it were a 1D sorted array
    left, right = 0, rows * cols - 1
    
    while left <= right:
        # Calculate mid point
        mid = (left + right) // 2
        
        # Convert 1D index to 2D coordinates
        row = mid // cols
        col = mid % cols
        
        # Get the current value
        current = matrix[row][col]
        
        # Compare and adjust search space
        if current == target:
            return (row, col)
        elif current < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Target not found
    return None