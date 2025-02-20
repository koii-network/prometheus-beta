def fibonacci_recursive(n):
    """
    Generate Fibonacci sequence using recursion.
    
    Args:
        n (int): Number of terms in the Fibonacci sequence to generate.
    
    Returns:
        list: A list containing the first n terms of the Fibonacci sequence.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    def fib(k):
        """
        Recursive helper function to calculate Fibonacci numbers.
        
        Args:
            k (int): The index of the Fibonacci number to calculate.
        
        Returns:
            int: The Fibonacci number at index k.
        """
        if k <= 1:
            return k
        return fib(k-1) + fib(k-2)
    
    return [fib(i) for i in range(n)]