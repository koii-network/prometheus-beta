def fibonacci_log_n(n):
    """
    Calculate the n-th Fibonacci number with O(log n) time complexity 
    using matrix exponentiation.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based index)
    
    Returns:
        int: The n-th Fibonacci number
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    # Helper function to multiply 2x2 matrices
    def matrix_multiply(a, b):
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ]
    
    # Helper function for matrix exponentiation
    def matrix_power(matrix, power):
        # Base case for matrix power
        if power == 1:
            return matrix
        
        # Recursively compute matrix power
        if power % 2 == 0:
            half = matrix_power(matrix, power // 2)
            return matrix_multiply(half, half)
        else:
            return matrix_multiply(matrix, matrix_power(matrix, power - 1))
    
    # Initial matrix representing the fibonacci recurrence
    base_matrix = [[1, 1], [1, 0]]
    
    # Compute the matrix power to get the (n-1)th fibonacci number
    result_matrix = matrix_power(base_matrix, n - 1)
    
    # Return the top-right element which is the nth fibonacci number
    return result_matrix[0][0]