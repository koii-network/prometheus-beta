def fibonacci_memoized(n):
    """
    Compute the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to compute (non-negative integer).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Memoization cache to store computed Fibonacci numbers
    memo = {}
    
    def fib(k):
        # If the number is already in the cache, return it
        if k in memo:
            return memo[k]
        
        # Base cases
        if k == 0:
            return 0
        if k == 1:
            return 1
        
        # Compute and cache the Fibonacci number
        memo[k] = fib(k-1) + fib(k-2)
        return memo[k]
    
    return fib(n)