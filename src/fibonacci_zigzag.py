def fibonacci_zigzag(n):
    """
    Generate Fibonacci numbers up to the n'th Fibonacci number in a zigzag pattern.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci numbers to generate.
    
    Returns:
        list: A list of Fibonacci numbers in a zigzag pattern.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle small input cases
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Initialize Fibonacci sequence
    fib = [0, 1]
    
    # Generate Fibonacci numbers
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    # Create zigzag pattern
    zigzag = []
    left, right = 0, len(fib) - 1
    going_right = True
    
    while left <= right:
        if going_right:
            zigzag.append(fib[left])
            left += 1
        else:
            zigzag.append(fib[right])
            right -= 1
        
        going_right = not going_right
    
    return zigzag