def fibonacci_dp(n):
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based index).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Initialize dynamic programming array
    fib = [0] * (n + 1)
    fib[1] = 1
    
    # Build Fibonacci sequence using dynamic programming
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]