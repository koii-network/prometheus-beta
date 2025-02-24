def fibonacci_zigzag(n):
    """
    Generate a list of Fibonacci numbers up to the n'th Fibonacci number in a zigzag pattern.
    
    Args:
        n (int): A positive integer specifying the number of Fibonacci terms to generate.
    
    Returns:
        list: A list of Fibonacci numbers in a zigzag pattern.
    
    Raises:
        ValueError: If n is not a positive integer.
    
    Examples:
        >>> fibonacci_zigzag(5)
        [1, 1, 2, 3, 5]
        >>> fibonacci_zigzag(7)
        [1, 1, 2, 3, 5, 8, 13]
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special cases for small n
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    # Initialize Fibonacci sequence
    fib = [1, 1]
    
    # Generate Fibonacci numbers
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    return fib[:n]