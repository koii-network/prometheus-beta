def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed numbers
    
    Returns:
        list: A Fibonacci subsequence satisfying the condition
    
    Raises:
        ValueError: If no such subsequence can be found
    """
    # Special case handling for small values
    if n == 0:
        return [0]
    if n == 1:
        return [1, 1]
    
    # Attempt to find a subsequence that satisfies the condition
    for length in range(2, 100):  # Reasonable upper limit for search
        # Start with initial Fibonacci sequence
        sequence = [0, 1]
        
        # Extend the sequence
        while len(sequence) < length:
            sequence.append(sequence[-1] + sequence[-2])
        
        # Check if the sum of even-indexed numbers matches n
        even_sum = sum(sequence[::2])
        
        if even_sum == n:
            return sequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found where sum of even-indexed numbers equals {n}")