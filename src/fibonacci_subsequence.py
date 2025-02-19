def fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence of length n.
    
    Args:
        n (int): The length of the Fibonacci subsequence to generate.
    
    Returns:
        list: A list containing the first n numbers of the Fibonacci subsequence.
    
    Raises:
        ValueError: If n is less than 0.
    """
    # Handle invalid input
    if n < 0:
        raise ValueError("Length of subsequence must be non-negative")
    
    # Handle special cases for small n
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Generate Fibonacci subsequence
    subsequence = [0, 1]
    while len(subsequence) < n:
        subsequence.append(subsequence[-1] + subsequence[-2])
    
    return subsequence