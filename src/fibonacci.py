def generate_fibonacci(n):
    """
    Generate the Fibonacci sequence recursively for a given number of terms.

    Args:
        n (int): Number of terms in the Fibonacci sequence to generate.
    
    Returns:
        list: A list of Fibonacci numbers.
    
    Raises:
        ValueError: If the input is negative.
        TypeError: If the input is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    # Base cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Recursive implementation
    def fibonacci_recursive(m):
        """Inner recursive helper function to generate Fibonacci numbers."""
        if m <= 2:
            return [0, 1][:m]
        
        # Recursively generate sequence up to current point
        sequence = fibonacci_recursive(m - 1)
        # Add next Fibonacci number
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
    
    return fibonacci_recursive(n)