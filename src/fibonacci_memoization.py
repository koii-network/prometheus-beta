def fibonacci_memo(n):
    """
    Compute the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based index).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Check for negative input
    if n < 0:
        raise ValueError("Fibonacci index must be non-negative")
    
    # Memoization cache
    memo = {}
    
    def fib(k):
        # Base cases
        if k == 0:
            return 0
        if k == 1:
            return 1
        
        # Check memoized result
        if k in memo:
            return memo[k]
        
        # Compute and memoize result
        memo[k] = fib(k-1) + fib(k-2)
        return memo[k]
    
    return fib(n)