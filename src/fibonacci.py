def fibonacci(n):
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    Args:
        n (int): The position of the Fibonacci number to calculate (0-indexed).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle base cases
    if n <= 1:
        return n
    
    # Use dynamic programming with constant space
    prev, curr = 0, 1
    
    # Iterate to calculate nth Fibonacci number
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr