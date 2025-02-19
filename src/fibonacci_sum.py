def fibonacci_sum(n):
    """
    Calculate the sum of the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci terms to sum.
    
    Returns:
        int: The sum of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    # Initialize first two Fibonacci numbers and sum
    fib_prev, fib_curr = 0, 1
    fib_sum = 0
    
    # Iterate and calculate sum of first n Fibonacci numbers
    for _ in range(n):
        fib_sum += fib_prev
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    
    return fib_sum