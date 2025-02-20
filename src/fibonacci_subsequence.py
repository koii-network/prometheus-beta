def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed numbers in the subsequence
    
    Returns:
        list: A Fibonacci subsequence meeting the specified condition
    
    Raises:
        ValueError: If no valid subsequence can be found
    """
    # If n is 0, return a trivial case
    if n == 0:
        return [0]
    
    # Try different subsequence lengths
    for length in range(2, 20):  # Reasonable upper limit to prevent infinite search
        # Initialize the first two numbers 
        a, b = 0, 1
        subsequence = [a, b]
        
        # Generate Fibonacci subsequence
        while len(subsequence) < length:
            next_num = a + b
            subsequence.append(next_num)
            a, b = b, next_num
        
        # Calculate sum of even-indexed numbers
        even_indexed_sum = sum(subsequence[::2])
        
        # Check if we found a matching subsequence
        if even_indexed_sum == n:
            return subsequence
    
    # If no valid subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")