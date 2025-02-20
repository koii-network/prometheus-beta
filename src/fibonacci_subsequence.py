def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed numbers
    
    Returns:
        list: A Fibonacci subsequence meeting the criteria
    
    Raises:
        ValueError: If no valid subsequence can be found
    """
    # If n is 0, return a trivial subsequence
    if n == 0:
        return [0]
    
    # Try different subsequence lengths and combinations
    for length in range(2, 20):  # Reasonable upper limit
        for start in range(2):  # Try starting with 0 or 1
            subsequence = [0, 1] if start == 0 else [1, 1]
            
            # Generate Fibonacci subsequence
            while len(subsequence) < length:
                subsequence.append(subsequence[-1] + subsequence[-2])
            
            # Check sum of even-indexed numbers
            even_sum = sum(subsequence[::2])
            
            if even_sum == n:
                return subsequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")