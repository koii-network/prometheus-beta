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
    
    # Handle special cases for small n
    if n == 1:
        return 0  # First Fibonacci number is 0
    if n == 2:
        return 1  # Sum of first two Fibonacci numbers is 0 + 1 = 1
    
    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    fib_sum = a + b  # Start with sum of first two numbers
    
    # Calculate Fibonacci sequence and running sum
    for _ in range(3, n + 1):
        a, b = b, a + b
        fib_sum += b
    
    return fib_sum