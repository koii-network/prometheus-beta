def generate_fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of Fibonacci terms to generate
    
    Returns:
        list: A list containing n Fibonacci terms
    
    Raises:
        ValueError: If n is less than 0
    """
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    if n == 0:
        return []
    
    if n == 1:
        return [0]
    
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence