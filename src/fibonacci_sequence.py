def generate_modified_fibonacci(n, k):
    """
    Generate a modified Fibonacci sequence with specific constraints.
    
    Args:
        n (int): Maximum length of the sequence
        k (int): Minimum sum of consecutive numbers
    
    Returns:
        list: Modified Fibonacci sequence meeting the given constraints
    
    Raises:
        ValueError: If n or k is not a positive integer
    """
    # Validate input parameters
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")
    
    # Initialize the sequence
    sequence = []
    
    # Special case handling
    if n >= 1:
        sequence.append(1)
    
    if n >= 2:
        sequence.append(1)
    
    # Generate the sequence
    while len(sequence) < n:
        # Calculate the next number
        next_num = sequence[-1] + sequence[-2]
        
        # Check if the sum of last two consecutive numbers is >= k
        if sequence[-1] + sequence[-2] >= k:
            sequence.append(next_num)
        else:
            break
    
    return sequence