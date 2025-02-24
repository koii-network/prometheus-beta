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
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Define a generator function to create Fibonacci sequence
    def fib_generator() -> Generator[int, None, None]:
        """
        Recursive generator for Fibonacci sequence.
        Uses memoization to achieve O(n) time complexity.
        """
        # Memoization cache to store previously computed Fibonacci numbers
        memo = {}
        
        def fib(k: int) -> int:
            """
            Recursive Fibonacci number generator with memoization.
            
            Args:
                k (int): Index of Fibonacci number to compute.
            
            Returns:
                int: Fibonacci number at index k.
            """
            # Base cases
            if k == 0:
                return 0
            if k == 1:
                return 1
            
            # Check memoized results first
            if k in memo:
                return memo[k]
            
            # Compute and memoize the result
            memo[k] = fib(k-1) + fib(k-2)
            return memo[k]
        
        # Generate Fibonacci numbers
        for i in range(n):
            yield fib(i)
    
    # Convert generator to list
    return list(fib_generator())