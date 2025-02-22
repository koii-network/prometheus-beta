def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed numbers.
    
    Returns:
        list: A Fibonacci subsequence meeting the criteria.
        
    Raises:
        ValueError: If no valid subsequence can be generated.
    """
    # Handle edge cases
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if n == 0:
        return [0]
    
    # Try different subsequence lengths
    for length in range(2, 100):  # Reasonable upper limit
        # Initialize the subsequence
        subsequence = [0, 1]
        
        # Extend the subsequence
        while len(subsequence) < length:
            subsequence.append(subsequence[-1] + subsequence[-2])
        
        # Calculate sum of even-indexed numbers
        even_sum = sum(subsequence[::2])
        
        # Check if we found a matching subsequence
        if even_sum == n:
            return subsequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")