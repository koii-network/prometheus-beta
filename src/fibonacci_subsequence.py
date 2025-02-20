def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers is equal to n.
    
    Args:
        n (int): The target sum of even-indexed numbers
    
    Returns:
        list: A Fibonacci subsequence that satisfies the condition
    
    Raises:
        ValueError: If no subsequence can be found
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for n = 0
    if n == 0:
        return [0]
    
    # Try different subsequence lengths
    for length in range(2, 100):  # Reasonable upper limit to prevent infinite search
        for start in range(2):  # Try different starting combinations
            subsequence = [0, 1] if start == 0 else [1, 1]
            
            # Generate rest of the subsequence
            while len(subsequence) < length:
                subsequence.append(subsequence[-1] + subsequence[-2])
            
            # Calculate sum of even-indexed numbers
            even_sum = sum(subsequence[::2])
            
            if even_sum == n:
                return subsequence
    
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")