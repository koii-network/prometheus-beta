def fibonacci_memoized(n):
    """
    Compute the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based index).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Fibonacci index must be non-negative")
    
    # Memoization cache to store previously computed Fibonacci numbers
    memo = {}
    
    def fib(k):
        # Check if the value is already in the memoization cache
        if k in memo:
            return memo[k]
        
        # Base cases
        if k == 0:
            return 0
        if k == 1:
            return 1
        
        # Recursively compute Fibonacci number with memoization
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]
    
    return fib(n)