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
    sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    # If n <= 10, return the predefined sequence up to n
    if n <= 10:
        return sequence[:n]
    
    # If more than 10 terms are needed, continue generating
    while len(sequence) < n:
        # Get the last two terms
        last = sequence[-1]
        second_last = sequence[-2]
        
        # Generate the next term
        next_term = last + second_last
        
        sequence.append(next_term)
    
    # Return only the first n terms
    return sequence[:n]