def fibonacci_sequence(n):
    """
    Generate the first n numbers of the Fibonacci sequence using recursion.
    
    Args:
        n (int): Number of Fibonacci sequence elements to generate.
    
    Returns:
        list: A list of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    """
    # Special case for n = 0
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Memoization dictionary to store previously computed Fibonacci numbers
    memo = {}
    
    def fib(k):
        """
        Recursive helper function to compute Fibonacci numbers with memoization.
        
        Args:
            k (int): Index of the Fibonacci number to compute.
        
        Returns:
            int: The k-th Fibonacci number.
        """
        # Base cases
        if k == 0:
            return 0
        if k == 1:
            return 1
        
        # Check memoized results to avoid recomputing
        if k in memo:
            return memo[k]
        
        # Recursive computation with memoization
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]
    
    # Generate sequence using the helper function
    return [fib(i) for i in range(n)]