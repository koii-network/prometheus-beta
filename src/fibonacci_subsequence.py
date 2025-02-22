def fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence of length n.
    
    Args:
        n (int): The length of the Fibonacci subsequence to generate.
    
    Returns:
        list: A list of Fibonacci numbers of length n.
    
    Raises:
        ValueError: If n is less than 1.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Length of subsequence must be at least 1")
    
    # Handle cases for small n
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Generate Fibonacci subsequence
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    return fib_seq