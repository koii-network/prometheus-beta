def fibonacci(n):
    """
    Calculate the nth Fibonacci number recursively.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based index).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Handle invalid input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Base cases
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative indices")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)