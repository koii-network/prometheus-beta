from typing import List, Dict

def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci sequence elements to generate.
    
    Returns:
        List[int]: A list of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Memoization cache to store computed Fibonacci numbers
    memo: Dict[int, int] = {}
    
    def fib(k: int) -> int:
        """
        Recursive helper function to compute Fibonacci numbers with memoization.
        
        Args:
            k (int): Index of the Fibonacci number to compute.
        
        Returns:
            int: The kth Fibonacci number.
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
        result = fib(k - 1) + fib(k - 2)
        memo[k] = result
        return result
    
    # Generate the first n Fibonacci numbers
    return [fib(i) for i in range(n)]