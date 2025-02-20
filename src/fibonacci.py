from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_sequence(n):
    """
    Generate the first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci sequence elements to generate. 
                 Must be a non-negative integer.
    
    Returns:
        list: A list of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case handling
    if n == 0:
        return []
    
    # Direct return for small sequences
    if n == 1:
        return [0]
    
    if n == 2:
        return [0, 1]
    
    # Recursive generation of Fibonacci sequence
    def _fibonacci_generator(num):
        if num <= 1:
            return 0 if num == 0 else 1
        return _fibonacci_generator(num - 1) + _fibonacci_generator(num - 2)
    
    # Generate sequence using list comprehension
    return [_fibonacci_generator(i) for i in range(n)]