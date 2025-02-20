def generate_fibonacci_like_sequence(n: int, k: int) -> list:
    """
    Generate a Fibonacci-like sequence with specific constraints.
    
    Args:
        n (int): Maximum length of the sequence
        k (int): Minimum sum of consecutive numbers
    
    Returns:
        list: A sequence of numbers meeting the specified conditions
    
    Raises:
        ValueError: If n or k is less than 1
    """
    # Validate input
    if n < 1 or k < 1:
        raise ValueError("n and k must be positive integers")
    
    # Initialize sequence
    sequence = []
    
    # Start with the first two numbers: 1, 1
    sequence.append(1)
    if n > 1:
        sequence.append(1)
    
    # Generate sequence
    while len(sequence) < n:
        # Compute next number
        next_num = sequence[-1] + sequence[-2]
        
        # Check if the sum of last two consecutive numbers meets the condition
        if next_num >= k:
            sequence.append(next_num)
        else:
            break
    
    return sequence