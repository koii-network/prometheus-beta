def fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence of length n.
    
    Args:
        n (int): The length of the subsequence to generate.
    
    Returns:
        list: A list of n Fibonacci numbers.
    
    Raises:
        ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("Subsequence length must be at least 1")
    
    # Handle the first two numbers of the Fibonacci sequence
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Generate the full subsequence
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    return fib_seq