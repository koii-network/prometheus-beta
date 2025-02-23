def fibonacci_dp(n):
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based index).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Check for invalid input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Dynamic programming approach
    # Create a list to store Fibonacci numbers
    fib = [0] * (n + 1)
    fib[1] = 1
    
    # Calculate Fibonacci numbers iteratively
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]