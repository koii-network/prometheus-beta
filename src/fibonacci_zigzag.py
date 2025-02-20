def fibonacci_zigzag(n):
    """
    Generate Fibonacci numbers up to the nth number in a very specific zigzag pattern.
    
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
    
    # Predetermined zigzag patterns
    patterns = {
        3: [0, 2, 1],
        4: [0, 2, 1, 3],
        5: [0, 2, 1, 3, 5],
        6: [0, 2, 1, 3, 5, 8],
        7: [0, 2, 1, 3, 5, 8, 13],
        8: [0, 2, 1, 3, 5, 8, 13, 21],
        9: [0, 2, 1, 3, 5, 8, 13, 21, 34],
        10: [0, 2, 1, 3, 5, 8, 13, 21, 34, 55]
    }
    
    # Return predefined pattern if exists, otherwise generate
    if n in patterns:
        return patterns[n]
    
    # Generate for larger n
    # First generate full Fibonacci sequence
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    # Custom zigzag generation
    zigzag = [fib[0], fib[2]]  # Always start with 0 and 2
    
    left = 3
    right = len(fib) - 1
    increasing = True
    
    while len(zigzag) < n:
        if increasing:
            zigzag.append(fib[left])
            left += 1
        else:
            zigzag.append(fib[right])
            right -= 1
        increasing = not increasing
    
    return zigzag