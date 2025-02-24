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
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")

    # Special case for zero length
    if n == 0:
        return []

    # Initialize the sequence
    sequence = [1]
    
    # If n is 1, return the initial value
    if n == 1:
        return sequence
    
    # Add second number only if needed for length or sum constraint
    if n > 1:
        sequence.append(1)
    
    # Generate the sequence
    while len(sequence) < n:
        # Check if the sum of last two numbers meets the constraint
        if sequence[-1] + sequence[-2] < k:
            # Break if the constraint cannot be met
            break
        
        # Calculate the next number in the sequence
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence