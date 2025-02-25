def matrix_multiply(a, b):
    """
    Multiply two 2x2 matrices efficiently.
    
    Args:
        a (list of lists): First 2x2 matrix
        b (list of lists): Second 2x2 matrix
    
    Returns:
        list of lists: Resulting 2x2 matrix
    """
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], 
         a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], 
         a[1][0] * b[0][1] + a[1][1] * b[1][1]]
    ]

def matrix_power(matrix, n):
    """
    Compute matrix raised to the power n using fast exponentiation.
    
    Args:
        matrix (list of lists): Base 2x2 matrix
        n (int): Exponent
    
    Returns:
        list of lists: Matrix raised to the power n
    """
    # Base cases
    if n == 0:
        return [[1, 0], [0, 1]]  # Identity matrix
    if n == 1:
        return matrix
    
    # Recursive fast exponentiation
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return matrix_multiply(half, half)
    else:
        return matrix_multiply(matrix, matrix_power(matrix, n - 1))

def fibonacci(n):
    """
    Calculate the n-th Fibonacci number using matrix exponentiation.
    Provides O(log n) time complexity.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-indexed)
    
    Returns:
        int: The n-th Fibonacci number
    
    Raises:
        ValueError: If n is negative
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases for first few Fibonacci numbers
    if n <= 1:
        return n
    
    # Base transformation matrix for Fibonacci sequence
    base_matrix = [[1, 1], [1, 0]]
    
    # Compute the matrix power
    result_matrix = matrix_power(base_matrix, n - 1)
    
    # Return the top-left element, which is the n-th Fibonacci number
    return result_matrix[0][0]