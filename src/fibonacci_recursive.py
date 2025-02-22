def fibonacci_recursive(n: int) -> int:
    """
    Generate Fibonacci numbers using recursion.
    
    Args:
        n (int): The nth Fibonacci number to generate (1-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Raises:
        ValueError: If n is less than 1
    """
    # Handle invalid input
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Base cases
    if n == 1 or n == 2:
        return 1
    
    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)