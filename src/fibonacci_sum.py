def fibonacci_sum(n):
    """
    Calculate the sum of the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci numbers to sum.
    
    Returns:
        int: The sum of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle first few cases
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Initialize Fibonacci sequence and sum
    fib_a, fib_b = 0, 1
    total_sum = 0
    
    # Compute Fibonacci sum for first n numbers
    for _ in range(n):
        total_sum += fib_a
        fib_a, fib_b = fib_b, fib_a + fib_b
    
    return total_sum