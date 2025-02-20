def fibonacci_reverse(n):
    """
    Generate Fibonacci sequence up to the Nth element in reverse order.
    
    Args:
        n (int): The number of Fibonacci elements to generate.
    
    Returns:
        list: Fibonacci sequence in reverse order.
    
    Raises:
        ValueError: If n is negative.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle edge cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    # Generate Fibonacci sequence
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Return sequence in reverse order
    return list(reversed(fib_sequence[:n]))