def fibonacci(n):
    """
    Compute the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based index).
    
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
    
    # Memoization cache
    memo = {}
    
    def fib(k):
        # Check if already computed
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