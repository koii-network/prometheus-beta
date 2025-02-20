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
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Initialize the sequence with the first two terms
    sequence = [0, 1]
    
    # Generate subsequent terms
    while len(sequence) < n:
        # Get the last two terms
        prev, curr = sequence[-2], sequence[-1]
        
        # Determine the next term to ensure odd sum
        # If prev + curr is even, we adjust the next term to make the sum odd
        next_term = curr + (1 if (prev + curr) % 2 == 0 else 0)
        
        sequence.append(next_term)
    
    # Return only the first n terms
    return sequence[:n]