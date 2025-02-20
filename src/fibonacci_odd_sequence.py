def generate_odd_fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence containing only odd numbers.
    
    Args:
        n (int): The number of odd Fibonacci numbers to generate.
    
    Returns:
        list: A list of n odd Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases for small n
    if n == 0:
        return []
    if n == 1:
        return [1]
    
    # Initialize sequence with first two odd Fibonacci numbers
    sequence = [1, 1]
    
    # Continue generating until we have n odd numbers
    while len(sequence) < n:
        # Calculate next Fibonacci number that is odd
        next_num = sequence[-1] + sequence[-2]
        
        # Ensure only odd numbers are added
        if next_num % 2 != 0:
            sequence.append(next_num)
    
    return sequence