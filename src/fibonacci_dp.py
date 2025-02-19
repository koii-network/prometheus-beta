def fibonacci_dp(n):
    """
    Compute the nth Fibonacci number using an efficient dynamic programming approach.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based indexing).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle small n cases first
    if n <= 1:
        return n
    
    # Initialize dynamic programming array
    fib = [0] * (n + 1)
    fib[1] = 1
    
    # Fill the array using dynamic programming
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]