def generate_fibonacci(n):
    """
    Generate Fibonacci sequence using recursion for a given number of terms.
    
    Args:
        n (int): Number of Fibonacci terms to generate
    
    Returns:
        list: A list of Fibonacci sequence terms
    
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Number of terms must be an integer")
    
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    # Base cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Recursive helper function
    def fib(index):
        """
        Recursive helper function to generate Fibonacci numbers.
        
        Args:
            index (int): Index of the Fibonacci number to generate
        
        Returns:
            int: Fibonacci number at the given index
        """
        if index <= 1:
            return index
        return fib(index - 1) + fib(index - 2)
    
    # Generate the sequence
    return [fib(i) for i in range(n)]