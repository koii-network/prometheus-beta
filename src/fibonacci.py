def fibonacci_memoized(n):
    """
    Compute the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative")
    
    # Memoization cache
    memo = {}
    
    def fib(k):
        # Check if value is already computed
        if k in memo:
            return memo[k]
        
        # Base cases
        if k == 0:
            return 0
        if k == 1:
            return 1
        
        # Compute and memoize
        memo[k] = fib(k-1) + fib(k-2)
        return memo[k]
    
    return fib(n)