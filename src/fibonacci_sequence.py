from functools import lru_cache
from typing import List

@lru_cache(maxsize=None)
def fibonacci_generator(index: int) -> int:
    """
    Recursive memoized function to generate Fibonacci numbers.
    
    Args:
        index (int): The index of the Fibonacci number to generate.
    
    Returns:
        int: The Fibonacci number at the specified index.
    """
    if index <= 1:
        return index
    return fibonacci_generator(index - 1) + fibonacci_generator(index - 2)

def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci numbers to generate.
    
    Returns:
        List[int]: A list of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    return [fibonacci_generator(i) for i in range(n)]