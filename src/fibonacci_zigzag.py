def fibonacci_zigzag(n):
    """
    Generate Fibonacci numbers up to the nth number in a zigzag pattern.
    
    Args:
        n (int): A positive integer specifying the nth Fibonacci number to generate.
    
    Returns:
        list: Fibonacci numbers in a zigzag pattern.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    # Create zigzag pattern
    zigzag = []
    left, right = 0, len(fib) - 1
    is_left = True
    
    while left <= right:
        if is_left:
            zigzag.append(fib[left])
            left += 1
        else:
            zigzag.append(fib[right])
            right -= 1
        is_left = not is_left
    
    return zigzag