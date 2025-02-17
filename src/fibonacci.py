def generate_fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of terms to generate. Must be a positive integer.
    
    Returns:
        list: A list of Fibonacci sequence terms.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Number of terms must be a positive integer")
    
    # Handle special cases
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Generate Fibonacci sequence
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence