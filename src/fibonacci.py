def fibonacci(n, memo=None):
    """
    Compute the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based index).
        memo (dict, optional): Memoization dictionary to store computed values.
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Initialize memoization dictionary if not provided
    if memo is None:
        memo = {}
    
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Check if value is already memoized
    if n in memo:
        return memo[n]
    
    # Compute and memoize the result
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]