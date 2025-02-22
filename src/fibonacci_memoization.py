def fibonacci_memoized(n, memo=None):
    """
    Calculate the nth Fibonacci number using recursion and memoization.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based).
        memo (dict, optional): Memoization dictionary to store previously computed values.
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Initialize memoization dictionary if not provided
    if memo is None:
        memo = {}
    
    # Check for negative input
    if n < 0:
        raise ValueError("Fibonacci index must be non-negative")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Check if value is already memoized
    if n in memo:
        return memo[n]
    
    # Recursive calculation with memoization
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]