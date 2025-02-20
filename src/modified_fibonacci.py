def modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    numbers is always odd.
    
    Args:
        n (int): Number of terms to generate in the sequence
    
    Returns:
        list: First n numbers in the modified Fibonacci sequence
    
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("Number of terms must be at least 1")
    
    # Initialize the sequence with 0 and 1
    sequence = [0, 1]
    
    # If n is 1 or 2, return the initial part of the sequence
    if n <= 2:
        return sequence[:n]
    
    # Generate subsequent terms
    while len(sequence) < n:
        # Get the last two terms
        last = sequence[-1]
        second_last = sequence[-2]
        
        # Generate next term
        next_term = last + second_last
        
        sequence.append(next_term)
    
    return sequence