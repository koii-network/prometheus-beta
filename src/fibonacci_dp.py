def fibonacci_dp(n):
    """
    Compute the nth Fibonacci number using dynamic programming.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based index).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Fibonacci index must be non-negative")
    
    # Handle base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Use dynamic programming with constant space complexity
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b