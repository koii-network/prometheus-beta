def fibonacci_recursive(n):
    """
    Generate the Fibonacci sequence for a given number of terms using recursion.
    
    Args:
        n (int): Number of terms in the Fibonacci sequence to generate.
    
    Returns:
        list: A list containing the first n terms of the Fibonacci sequence.
    
    Raises:
        ValueError: If the input is less than 0.
    """
    if n < 0:
        raise ValueError("Number of terms must be a non-negative integer")
    
    def fib(k):
        """Internal recursive helper function to generate Fibonacci numbers."""
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)
    
    return [fib(i) for i in range(n)]