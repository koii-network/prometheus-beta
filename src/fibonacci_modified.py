def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence up to n where the sum of 
    any two consecutive numbers (starting from the third number) is 
    always divisible by 3.
    
    Args:
        n (int): The upper limit for the sequence length.
    
    Returns:
        list: Modified Fibonacci sequence.
    
    Raises:
        ValueError: If input is not a positive integer.
    """
    # Input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Initialize sequence with first two numbers
    sequence = [1, 1]
    
    while len(sequence) < n:
        # Calculate next number to ensure divisibility by 3
        next_num = sequence[-1] + sequence[-2]
        
        # Adjust the next number if the sum is not divisible by 3
        while (sequence[-1] + next_num) % 3 != 0:
            next_num += 1
        
        sequence.append(next_num)
    
    return sequence[:n]