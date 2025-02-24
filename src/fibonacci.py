from typing import List, Generator

def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci sequence elements to generate.
    
    Returns:
        List[int]: List of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Handle special cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Preallocate the list for efficiency
    fib_seq = [0] * n
    fib_seq[0] = 0
    fib_seq[1] = 1
    
    # Compute subsequent Fibonacci numbers
    for i in range(2, n):
        fib_seq[i] = fib_seq[i-1] + fib_seq[i-2]
    
    return fib_seq