def generate_fibonacci_sequence(n: int, k: int) -> list:
    """
    Generate a Fibonacci-like sequence with specific constraints.
    
    Args:
        n (int): Maximum length of the sequence
        k (int): Minimum sum of consecutive numbers
    
    Returns:
        list: A sequence of numbers meeting the specified constraints
    
    Raises:
        ValueError: If n or k is not a positive integer
    """
    # Validate input parameters
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")
    
    # Handle special cases
    if n == 1:
        return [1]
    
    # Initialize the sequence
    sequence = [1, 1]
    
    # Generate the sequence
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        
        # Check if the sum meets the constraint
        if next_num + sequence[-1] >= k:
            sequence.append(next_num)
        else:
            break
    
    return sequence