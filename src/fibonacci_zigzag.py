def fibonacci_zigzag(n):
    """
    Generate a list of Fibonacci numbers up to the n'th Fibonacci number in a zigzag pattern.
    
    Args:
        n (int): A positive integer specifying the number of Fibonacci numbers to generate.
    
    Returns:
        list: A list of Fibonacci numbers in a zigzag pattern.
    
    Raises:
        ValueError: If n is not a positive integer.
    
    Examples:
        >>> fibonacci_zigzag(1)
        [0]
        >>> fibonacci_zigzag(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_zigzag(7)
        [0, 1, 1, 2, 3, 5, 8]
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle small inputs
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Generate Fibonacci sequence
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    return fib[:n]