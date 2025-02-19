def search_matrix(matrix, target):
    """
    Search for a target integer in an M x N matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The integer to search for
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    
    Time Complexity: O(m * n)
    Space Complexity: O(1)
    """
    # Handle empty matrix
    if not matrix or not matrix[0]:
        return False
    
    # Iterate through each row and column
    for row in matrix:
        for num in row:
            if num == target:
                return True
    
    return False