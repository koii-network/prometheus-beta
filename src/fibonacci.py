def fibonacci_log_n(n):
    """
    Calculate the n-th Fibonacci number with O(log(n)) time complexity
    using matrix exponentiation method.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based)
    
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
    if n == 1:
        return 1
    
    def matrix_multiply(A, B):
        """Multiply 2x2 matrices"""
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]
    
    def matrix_power(matrix, power):
        """Compute matrix raised to a power using binary exponentiation"""
        # Start with the identity matrix
        result = [[1, 0], [0, 1]]
        
        while power > 0:
            # If power is odd, multiply result by current matrix
            if power % 2 == 1:
                result = matrix_multiply(result, matrix)
            
            # Square the matrix
            matrix = matrix_multiply(matrix, matrix)
            
            # Reduce the power
            power //= 2
        
        return result
    
    # Define the base transformation matrix
    base_matrix = [[1, 1], [1, 0]]
    
    # Compute the matrix power
    result_matrix = matrix_power(base_matrix, n - 1)
    
    # Return the top-right element (which is the n-th Fibonacci number)
    return result_matrix[0][0]