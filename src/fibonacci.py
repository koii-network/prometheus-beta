def fibonacci_generator(n):
    """
    Generate and return a list of the first n Fibonacci numbers.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: A list of the first n Fibonacci numbers
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Number of Fibonacci numbers must be non-negative")
    
    # Handle special cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Generate Fibonacci sequence
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    return fib