def generate_fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of terms to generate in the Fibonacci sequence.
    
    Returns:
        list: A list of Fibonacci numbers up to n terms.
    
    Raises:
        ValueError: If n is less than 0.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be a non-negative integer")
    
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