def find_fibonacci_arithmetic_progression(n):
    """
    Find the first n Fibonacci numbers that form an arithmetic progression.
    
    Args:
        n (int): Number of Fibonacci numbers to find
    
    Returns:
        list: A list of Fibonacci numbers forming an arithmetic progression
    
    Raises:
        ValueError: If n is less than 3 (minimum required to form an arithmetic progression)
    """
    if n < 3:
        raise ValueError("At least 3 numbers are required to form an arithmetic progression")
    
    # Generate Fibonacci sequence
    fib = [1, 1]  # Start with first two Fibonacci numbers
    
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    # Check for arithmetic progression
    for i in range(2, n):
        # Check if the difference between consecutive terms is constant
        if (fib[i] - fib[i-1]) != (fib[i-1] - fib[i-2]):
            return []
    
    return fib[:n]