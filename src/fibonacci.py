def fibonacci_recursive(n):
    """
    Generate Fibonacci sequence using recursion for a given number of terms.
    
    Args:
        n (int): Number of terms to generate in the Fibonacci sequence.
    
    Returns:
        list: A list of Fibonacci sequence terms.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    def fib(i):
        """
        Recursive helper function to generate Fibonacci numbers.
        
        Args:
            i (int): Index of the Fibonacci number to generate.
        
        Returns:
            int: Fibonacci number at index i.
        """
        if i <= 1:
            return i
        return fib(i - 1) + fib(i - 2)
    
    return [fib(i) for i in range(n)]