def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    Fibonacci numbers is always odd.
    
    Args:
        n (int): Number of terms to generate in the sequence
    
    Returns:
        list: First n numbers in the modified Fibonacci sequence
    
    Raises:
        ValueError: If n is less than 1
    """
    # Validate input
    if n < 1:
        raise ValueError("Number of terms must be at least 1")
    
    # Initialize the sequence with first two terms
    sequence = [0, 1]
    
    # Generate subsequent terms
    while len(sequence) < n:
        # Get the last two terms
        last = sequence[-1]
        second_last = sequence[-2]
        
        # Determine the next term to ensure odd sum of previous two terms
        next_term = last + second_last
        
        # Special rule: If the sum becomes even, adjust the next term
        if (last + second_last) % 2 == 0:
            next_term += 1
        
        sequence.append(next_term)
    
    # Return only the first n terms
    return sequence[:n]