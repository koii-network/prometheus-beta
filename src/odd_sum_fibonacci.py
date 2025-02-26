def generate_odd_sum_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    numbers follows a special parity rule.
    
    Args:
        n (int): Number of elements to generate in the sequence
    
    Returns:
        list: Modified Fibonacci sequence of length n
    
    Raises:
        ValueError: If n is less than 0
        TypeError: If input is not an integer
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Number of elements must be non-negative")
    
    # Handle edge cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Initialize the sequence
    sequence = [0, 1, 2]
    
    # Generate subsequent terms
    while len(sequence) < n:
        # Get the last two terms
        a, b = sequence[-2], sequence[-1]
        
        # Calculate the next term to ensure changing parity of consecutive sums
        next_term = a + b + (1 if (a + b) % 2 == (sequence[-3] + a) % 2 else 0)
        
        sequence.append(next_term)
    
    # Trim to n elements
    return sequence[:n]