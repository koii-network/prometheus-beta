def generate_fibonacci_sum_sequence(n: int, k: int) -> list:
    """
    Generate a Fibonacci-like sequence with specific constraints.

    Args:
        n (int): Maximum length of the sequence
        k (int): Minimum sum of consecutive numbers

    Returns:
        list: A sequence of numbers meeting the specified constraints

    Raises:
        ValueError: If n or k is negative
    """
    # Validate input parameters
    if n < 0 or k < 0:
        raise ValueError("Both n and k must be non-negative integers")

    # Handle trivial cases
    if n == 0:
        return []
    
    # Initialize the sequence with first number
    if k == 0:
        sequence = [0]
    else:
        sequence = [max(1, k // 2)]

    # Generate sequence
    while len(sequence) < n:
        # Compute the next number based on sum constraint
        next_num = max(sequence[-1] + 1, k - sequence[-1])
        
        # Stop if we can't generate a valid next number
        if sum(sequence[-2:]) < k and len(sequence) > 1:
            break
        
        sequence.append(next_num)

    return sequence