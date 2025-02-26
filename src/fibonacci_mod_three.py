def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence up to a given number with a special divisibility constraint.
    
    The sequence starts with [1, 1] and modifies subsequent numbers so that the sum of any two 
    consecutive numbers (starting from the third number) is always divisible by 3.
    
    Args:
        n (int): The maximum number of elements in the sequence to generate.
    
    Returns:
        list: A modified Fibonacci sequence satisfying the divisibility constraint.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Initialize the sequence with first two numbers
    sequence = [1, 1]
    
    # Generate the sequence
    while len(sequence) < n:
        # Calculate the next number to ensure sum of last two is divisible by 3
        next_num = sequence[-1] + sequence[-2]
        # Modify the next number if needed to make the sum divisible by 3
        if (sequence[-2] + sequence[-1]) % 3 != 0:
            next_num = 3 - (sequence[-2] + sequence[-1]) % 3 + sequence[-2] + sequence[-1]
        sequence.append(next_num)
    
    # Return only the first n elements
    return sequence[:n]