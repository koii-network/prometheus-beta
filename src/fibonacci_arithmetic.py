def fibonacci_arithmetic_progression(n):
    """
    Returns the first n Fibonacci numbers that form an arithmetic progression.
    
    Args:
        n (int): Number of Fibonacci numbers to find in the arithmetic progression
    
    Returns:
        list: List of Fibonacci numbers forming an arithmetic progression
    
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    # Initialize Fibonacci sequence
    fib = [1, 1]
    
    # Keep track of the last few Fibonacci numbers to check arithmetic progression
    while len(fib) < n:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    
    # Check if the first n numbers form an arithmetic progression
    for i in range(2, n):
        # Check if the difference between consecutive terms is constant
        if fib[i] - fib[i-1] != fib[1] - fib[0]:
            return []
    
    return fib[:n]