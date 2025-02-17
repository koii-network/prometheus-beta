def generate_fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of terms in the Fibonacci sequence to generate.
    
    Returns:
        list: A list of Fibonacci numbers.
    
    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    if n == 0:
        return []
    
    if n == 1:
        return [0]
    
    if n == 2:
        return [0, 1]
    
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < n:
        next_term = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_term)
    
    return fibonacci_seq