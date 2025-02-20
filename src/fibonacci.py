def generate_fibonacci(n):
    """
    Generate Fibonacci sequence using recursion for a given number of terms.
    
    Args:
        n (int): Number of terms to generate in the Fibonacci sequence.
    
    Returns:
        list: A list of Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    # Define inner recursive function
    def fib_recursive(count):
        # Base cases
        if count <= 0:
            return []
        elif count == 1:
            return [0]
        elif count == 2:
            return [0, 1]
        
        # Recursive case
        sequence = fib_recursive(count - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
    
    return fib_recursive(n)