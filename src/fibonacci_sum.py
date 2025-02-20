def fibonacci_sum(n):
    """
    Calculate the sum of the first 'n' numbers in the Fibonacci sequence.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci numbers to sum.
    
    Returns:
        int: The sum of the first 'n' Fibonacci numbers.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Initialize Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to n numbers
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    # Return the sum of the first n Fibonacci numbers
    return sum(fib_sequence[:n])