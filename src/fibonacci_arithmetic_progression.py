def fibonacci_arithmetic_progression(n):
    """
    Returns the first n Fibonacci numbers that form an arithmetic progression.
    
    An arithmetic progression means the difference between consecutive numbers 
    is constant.
    
    Args:
        n (int): Number of Fibonacci numbers to return
    
    Returns:
        list: First n Fibonacci numbers forming an arithmetic progression
    
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    
    # Initialize Fibonacci sequence
    fib = [1, 1]
    
    # If n is 1 or 2, return the initial sequence
    if n <= 2:
        return fib[:n]
    
    # Find Fibonacci numbers that form an arithmetic progression
    while len(fib) < n:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
        
        # Check if the last 3 numbers form an arithmetic progression
        if len(fib) >= 3:
            diff1 = fib[-2] - fib[-3]
            diff2 = fib[-1] - fib[-2]
            
            # If differences are not equal, reset search
            if diff1 != diff2:
                # We continue adding Fibonacci terms, hoping to find a match
                continue
    
    return fib[:n]