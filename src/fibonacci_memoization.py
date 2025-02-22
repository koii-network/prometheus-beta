def fibonacci_memoized(n):
    """
    Compute the nth Fibonacci number using memoization.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Check for invalid input
    if not isinstance(n, int):
        raise TypeError("Input must be a non-negative integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Memoization cache to store previously computed Fibonacci numbers
    memo = {}
    
    def fib(k):
        # Check if the value is already in the memo
        if k in memo:
            return memo[k]
        
        # Base cases
        if k == 0:
            return 0
        if k == 1:
            return 1
        
        # Compute and memoize the result
        result = fib(k-1) + fib(k-2)
        memo[k] = result
        return result
    
    return fib(n)