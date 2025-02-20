def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence up to n numbers,
    where the sum of any two consecutive numbers (starting from the third)
    is always divisible by 3.
    
    Args:
        n (int): Number of elements to generate in the sequence
    
    Returns:
        list: Modified Fibonacci sequence
    
    Raises:
        ValueError: If n is less than 1
    """
    # Validate input
    if n < 1:
        raise ValueError("Number of elements must be at least 1")
    
    # Special cases for small n
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    # Initialize sequence
    sequence = [1, 1]
    
    # Generate the sequence
    while len(sequence) < n:
        # Calculate the next number to ensure the sum of last two is divisible by 3
        next_num = sequence[-1] + sequence[-2]
        
        # Adjust the next number if needed to make sum divisible by 3
        while (sequence[-1] + sequence[-2]) % 3 != 0:
            next_num += 1
        
        sequence.append(next_num)
    
    return sequence