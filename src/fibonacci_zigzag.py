def fibonacci_zigzag(n):
    """
    Generate Fibonacci numbers up to the nth number in a zigzag pattern.
    
    Args:
        n (int): A positive integer specifying the number of Fibonacci elements to generate.
    
    Returns:
        list: A list of Fibonacci numbers in a zigzag pattern.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle trivial cases
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Generate Fibonacci sequence
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    # Create zigzag pattern
    zigzag = []
    left = 0
    right = len(fib) - 1
    direction = 1
    
    while left <= right:
        if direction == 1:
            zigzag.append(fib[left])
            left += 1
        else:
            zigzag.append(fib[right])
            right -= 1
        direction *= -1
    
    return zigzag