def generate_fibonacci_square_pairs(n):
    """
    Generate a Fibonacci-like sequence where the sum of consecutive pairs is a perfect square.
    
    Args:
        n (int): Number of elements to generate in the sequence
    
    Returns:
        list: A list of n numbers in the sequence
    
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("Number of elements must be at least 1")
    
    # Initialize the sequence
    sequence = [1, 1]
    
    # Generate the rest of the sequence
    while len(sequence) < n:
        # Find the next number that makes the sum of consecutive pairs a perfect square
        def is_perfect_square(num):
            return int(num**0.5)**2 == num
        
        # Start checking from the last generated number
        next_num = sequence[-1] + sequence[-2]
        while not is_perfect_square(sequence[-1] + next_num):
            next_num += 1
        
        sequence.append(next_num)
    
    # Return only the first n elements
    return sequence[:n]