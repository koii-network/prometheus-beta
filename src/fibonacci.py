def generate_fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of Fibonacci terms to generate
    
    Returns:
        list: A list of Fibonacci numbers
    
    Raises:
        ValueError: If n is less than 0
    """
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    # Handle special cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Generate Fibonacci sequence
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence