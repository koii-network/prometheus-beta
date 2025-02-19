def fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence of length n.
    
    Args:
        n (int): The length of the subsequence to generate.
    
    Returns:
        list: A list containing the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is less than or equal to 0.
    """
    if n <= 0:
        raise ValueError("Subsequence length must be a positive integer")
    
    # Handle the first two cases specifically
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Generate subsequence for n > 2
    subsequence = [0, 1]
    while len(subsequence) < n:
        next_num = subsequence[-1] + subsequence[-2]
        subsequence.append(next_num)
    
    return subsequence