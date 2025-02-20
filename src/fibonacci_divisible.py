def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence up to n where the sum of any two 
    consecutive numbers (starting from the third number) is divisible by 3.
    
    Args:
        n (int): The maximum number of elements to generate in the sequence
    
    Returns:
        list: A modified Fibonacci sequence
    
    Raises:
        ValueError: If input is not a positive integer
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case handling for small sequences
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    # Initialize the sequence
    sequence = [1, 1]
    
    while len(sequence) < n:
        # Calculate next number to ensure sum of last two is divisible by 3
        next_num = 3 - (sequence[-1] + sequence[-2]) % 3
        sequence.append(next_num)
    
    return sequence[:n]