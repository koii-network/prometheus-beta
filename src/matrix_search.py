def search_matrix(matrix, target):
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of unique integers 
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target is in the matrix, False otherwise
    
    Time Complexity: O(T * R) where T is number of rows and R is number of columns
    Space Complexity: O(1)
    """
    # Handle empty matrix case
    if not matrix or not matrix[0]:
        return False
    
    # Iterate through each row
    for row in matrix:
        # Iterate through each column in the row
        for element in row:
            # If target is found, return True
            if element == target:
                return True
    
    # Target not found after searching entire matrix
    return False