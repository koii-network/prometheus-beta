def fibonacci_recursive(n):
    """
    Generate Fibonacci sequence up to n terms using recursion.
    
    Args:
        n (int): Number of terms to generate in the Fibonacci sequence.
    
    Returns:
        list: A list of Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    def fib(count):
        """Inner recursive function to generate Fibonacci numbers."""
        if count <= 1:
            return count
        return fib(count - 1) + fib(count - 2)
    
    return [fib(i) for i in range(n)]