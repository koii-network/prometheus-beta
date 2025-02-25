def compute_fibonacci(n):
    """
    Compute the nth Fibonacci number using an efficient dynamic programming approach.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-indexed).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle base cases
    if n <= 1:
        return n
    
    # Dynamic programming with constant space
    prev, curr = 0, 1
    
    # Compute Fibonacci number iteratively
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr