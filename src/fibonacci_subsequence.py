def fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence of length n.
    
    Args:
        n (int): The length of the Fibonacci subsequence to generate.
    
    Returns:
        list: A list containing the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is less than or equal to 0.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Length must be a positive integer")
    
    # Handle special cases for small n
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Generate Fibonacci subsequence
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    return fib_seq