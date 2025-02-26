def generate_odd_sum_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    numbers is always odd.
    
    Args:
        n (int): Number of elements to generate in the sequence
    
    Returns:
        list: Modified Fibonacci sequence of length n
    
    Raises:
        ValueError: If n is less than 0
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
    sequence = [0, 1]
    
    # Generate subsequent terms
    while len(sequence) < n:
        # Get the last two terms
        a, b = sequence[-2], sequence[-1]
        
        # Calculate the next term with the odd sum rule
        # We ensure the next term makes the sum of last two terms odd
        next_term = a + b + (1 if (a + b) % 2 == 0 else 0)
        
        sequence.append(next_term)
    
    return sequence