def fibonacci_dp(n):
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    Args:
        n (int): The position of the Fibonacci number to calculate (0-indexed).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Check for negative input
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Handle base cases
    if n <= 1:
        return n
    
    # Initialize dynamic programming array
    fib = [0] * (n + 1)
    fib[1] = 1
    
    # Build up Fibonacci sequence
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]