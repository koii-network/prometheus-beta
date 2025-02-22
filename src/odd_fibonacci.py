def generate_odd_fibonacci(n):
    """
    Generate a Fibonacci sequence of length n containing only odd numbers.
    
    Args:
        n (int): The number of odd Fibonacci numbers to generate.
    
    Returns:
        list: A list of n odd Fibonacci numbers.
    
    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases for small sequences
    if n == 0:
        return []
    if n == 1:
        return [1]
    
    # Initialize the sequence with the first two odd Fibonacci numbers
    sequence = [1, 1]
    
    # Generate the rest of the sequence
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        
        # Skip even numbers, find the next odd number
        while next_num % 2 == 0:
            next_num += 1
        
        sequence.append(next_num)
    
    return sequence