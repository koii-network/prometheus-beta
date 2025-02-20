from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_sequence(n):
    """
    Generate the first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci sequence elements to generate.
    
    Returns:
        list: A list of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Special case handling for small n values
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Recursive generation with memoization
    def fib(k):
        if k <= 1:
            return k
        return fib(k-1) + fib(k-2)
    
    return [fib(i) for i in range(n)]