import math

def generate_fibonacci_square_pairs(n):
    """
    Generate a Fibonacci-like sequence where the sum of consecutive pairs is a perfect square.
    
    Args:
        n (int): Number of elements to generate in the sequence
    
    Returns:
        list: A sequence of n numbers where consecutive pair sums are perfect squares
    
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    # Initial sequence start
    sequence = [1, 1]
    
    # Generate the rest of the sequence
    while len(sequence) < n:
        # Get the last two numbers
        a, b = sequence[-2], sequence[-1]
        
        # Try next candidate numbers that satisfy the square sum condition
        next_num = a + b
        
        # Ensure we find a number that creates a perfect square sum with previous number
        while True:
            # Check if the sum with the previous number is a perfect square
            sum_with_prev = next_num + b
            sqrt = int(math.sqrt(sum_with_prev))
            
            if sqrt * sqrt == sum_with_prev:
                sequence.append(next_num)
                break
            
            next_num += 1
    
    # Return only the first n elements
    return sequence[:n]