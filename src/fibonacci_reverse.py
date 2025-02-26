def fibonacci_reverse(n):
    """
    Generate a reversed Fibonacci sequence up to the nth element.
    
    Args:
        n (int): The number of Fibonacci elements to generate.
    
    Returns:
        list: A list of Fibonacci numbers in reverse order.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle special cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [1, 0]
    
    # Generate Fibonacci sequence
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Compute larger Fibonacci numbers and then reverse
    full_sequence = []
    current_value = fib_sequence[-1]
    while len(full_sequence) < n:
        full_sequence.append(current_value)
        
        # Find previous Fibonacci number
        fib_idx = fib_sequence.index(current_value) if current_value in fib_sequence else -1
        if fib_idx > 0:
            current_value = fib_sequence[fib_idx - 1]
        elif fib_idx == 0:
            current_value = 0
    
    return full_sequence