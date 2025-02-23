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
    
    if n == 0:
        return [0]
    
    # Try different subsequence lengths
    for length in range(2, 100):  # Reasonable upper limit to prevent infinite loop
        # Generate candidate subsequences
        for start_index in range(length):
            subsequence = [0] * length
            
            # Set initial Fibonacci-like conditions
            subsequence[start_index] = n
            
            # Try to generate a valid subsequence
            try:
                # Fill in other values following Fibonacci-like rule
                for i in range(length):
                    if i == start_index:
                        continue
                    
                    # If before start_index, use left-side Fibonacci generation
                    if i < start_index:
                        if i + 1 < start_index:
                            subsequence[i] = subsequence[i+1] - subsequence[start_index]
                        else:
                            subsequence[i] = subsequence[start_index]
                    
                    # If after start_index, use right-side Fibonacci generation
                    if i > start_index:
                        if i - 1 > start_index:
                            subsequence[i] = subsequence[i-1] + subsequence[i-2]
                        else:
                            subsequence[i] = subsequence[start_index]
                
                # Verify the condition
                even_sum = sum(subsequence[j] for j in range(length) if j % 2 == 0)
                
                if even_sum == n:
                    return subsequence
            
            except Exception:
                # If generation fails, continue to next iteration
                continue
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found for input {n}")