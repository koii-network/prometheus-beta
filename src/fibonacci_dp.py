def fibonacci_dynamic_programming(n):
    """
    Compute the nth Fibonacci number using an efficient dynamic programming approach.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based indexing).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Check for invalid input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle base cases
    if n <= 1:
        return n
    
    # Initialize dynamic programming array
    fib = [0] * (n + 1)
    fib[1] = 1
    
    # Build Fibonacci sequence iteratively
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]