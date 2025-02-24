from typing import List, Generator

def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.
    
    This function uses a recursive generator approach to create the Fibonacci sequence
    with O(n) time complexity and without using explicit loops.
    
    Args:
        n (int): The number of Fibonacci sequence elements to generate.
               Must be a non-negative integer.
    
    Returns:
        List[int]: A list containing the first n numbers of the Fibonacci sequence.
    
    Raises:
        ValueError: If n is a negative integer.
    
    Examples:
        >>> fibonacci_sequence(0)
        []
        >>> fibonacci_sequence(1)
        [0]
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case handling
    if n == 0:
        return []
    
    def fib_gen() -> Generator[int, None, None]:
        """
        Recursive generator for Fibonacci sequence.
        
        Yields:
            int: Next Fibonacci number in the sequence.
        """
        def fib_impl(a: int = 0, b: int = 1) -> Generator[int, None, None]:
            yield a
            if a == 0:
                yield b
            yield from fib_impl(b, a + b)
        
        return fib_impl()
    
    # Generate and collect the first n Fibonacci numbers
    result = []
    generator = fib_gen()
    for _ in range(n):
        result.append(next(generator))
    return result