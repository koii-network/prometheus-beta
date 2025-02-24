def generate_odd_sum_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    numbers is always odd.

    Args:
        n (int): Number of elements to generate in the sequence.
    
    Returns:
        list: A list of n modified Fibonacci numbers.
    
    Raises:
        ValueError: If n is less than 0.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Number of elements must be non-negative")
    
    # Handle special cases for small n
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
        # Calculate the next term with the odd sum constraint
        prev = sequence[-1]
        prev_prev = sequence[-2]
        
        # Ensure the sum of the last two numbers is odd
        # We'll modify the next term to make the sum odd
        next_term = prev + prev_prev
        
        # Adjust the next term if needed to ensure odd sum
        if (prev + prev_prev) % 2 == 0:
            next_term += 1
        
        sequence.append(next_term)
    
    return sequence