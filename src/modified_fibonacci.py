def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    numbers is always odd.
    
    Args:
        n (int): Number of elements to generate in the sequence
    
    Returns:
        list: First n numbers in the modified Fibonacci sequence
    
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    
    # Initialize the sequence
    sequence = [0]
    
    # If n > 1, add the first element
    if n > 1:
        sequence.append(1)
    
    # Generate the rest of the sequence
    while len(sequence) < n:
        # Apply a special modification to ensure the sum of last two numbers is odd
        next_num = sequence[-1] + sequence[-2]
        
        # If the sum is even, we'll add 1 to make it odd
        if (sequence[-1] + sequence[-2]) % 2 == 0:
            next_num += 1
        
        sequence.append(next_num)
    
    return sequence