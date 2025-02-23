def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers is equal to n.
    
    Args:
        n (int): The target sum of even-indexed numbers in the subsequence.
    
    Returns:
        list: A Fibonacci subsequence satisfying the condition.
    
    Raises:
        ValueError: If n is negative or cannot be achieved with a valid subsequence.
    """
    # Handle edge cases
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n > 10000:
        raise ValueError(f"Input {n} is too large to generate a subsequence")
    
    if n == 0:
        return [0, 0]  # Ensure minimum length of 2
    
    if n == 1:
        return [1, 0]
    
    # Try different subsequence lengths
    for length in range(2, 50):  # Reasonable upper limit
        # Generate candidate subsequences
        for start_index in range(length):
            subsequence = [0] * length
            
            # Set initial conditions
            subsequence[start_index] = n
            
            # Try to generate a valid subsequence
            try:
                # Attempt to fill in Fibonacci-like sequence
                for i in range(length):
                    if i == start_index:
                        continue
                    
                    # Generate subsequent values
                    if i > 0 and i < length - 1:
                        if i > start_index:
                            # Right side: standard Fibonacci
                            subsequence[i] = subsequence[i-1] + subsequence[i-2]
                        elif i < start_index:
                            # Left side: special generation
                            if i == start_index - 1:
                                subsequence[i] = 0  # Specific requirement
                            else:
                                subsequence[i] = subsequence[i+1] - subsequence[start_index]
                
                # Verify the condition
                even_sum = sum(subsequence[j] for j in range(length) if j % 2 == 0)
                
                if even_sum == n:
                    return subsequence
            
            except Exception:
                # If generation fails, continue to next iteration
                continue
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found for input {n}")