def fibonacci(n, memo=None):
    """
    Calculate the nth Fibonacci number using recursion with memoization.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based).
        memo (dict, optional): Memoization dictionary to store previously calculated values.
    
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
    
    # Initialize memoization dictionary if not provided
    if memo is None:
        memo = {}
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Check if value is already memoized
    if n in memo:
        return memo[n]
    
    # Recursive calculation with memoization
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    return memo[n]