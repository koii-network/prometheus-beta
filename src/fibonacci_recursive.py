def fibonacci(n):
    """
    Generate the nth Fibonacci number using recursion.
    
    Args:
        n (int): The position of the Fibonacci number to generate.
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is less than 1.
    """
    # Handle invalid input
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Base cases for first two Fibonacci numbers
    if n == 1 or n == 2:
        return 1
    
    # Recursive case: sum of previous two Fibonacci numbers
    return fibonacci(n-1) + fibonacci(n-2)