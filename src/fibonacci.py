def recursive_fibonacci(n):
    """
    Calculate the nth Fibonacci number using a recursive approach.

    The Fibonacci sequence starts with 0 and 1, where each subsequent 
    number is the sum of the two preceding ones.

    Args:
        n (int): The index of the Fibonacci number to calculate (0-based index).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.

    Examples:
        >>> recursive_fibonacci(0)
        0
        >>> recursive_fibonacci(1)
        1
        >>> recursive_fibonacci(5)
        5
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)