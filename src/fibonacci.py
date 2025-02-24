def memoized_fibonacci(n):
    """
    Compute the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based).
    
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
    memo = {0: 0, 1: 1}
    
    # Compute Fibonacci numbers up to n
    def fibonacci(k):
        # Check if already computed
        if k in memo:
            return memo[k]
        
        # Compute and memoize
        memo[k] = fibonacci(k-1) + fibonacci(k-2)
        return memo[k]
    
    return fibonacci(n)