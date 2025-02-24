def generate_fibonacci_sequence(n, k):
    """
    Generate a Fibonacci-like sequence with specific constraints.

    Args:
        n (int): Maximum length of the sequence
        k (int): Minimum sum of consecutive numbers

    Returns:
        list: A list of numbers forming the constrained Fibonacci sequence

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

    # Special case handling for very small n
    if n == 0:
        return sequence
    
    # Start with first two numbers 
    sequence.append(1)
    if n == 1:
        return sequence
    
    sequence.append(1)
    
    # Generate the sequence
    while len(sequence) < n:
        # Calculate the next number in the sequence
        next_num = sequence[-1] + sequence[-2]
        
        # Check if the sum of last two numbers meets the constraint
        if next_num >= k:
            sequence.append(next_num)
        else:
            break

    return sequence