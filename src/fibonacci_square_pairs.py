import math

def is_perfect_square(num):
    """Check if a number is a perfect square."""
    root = int(math.sqrt(num))
    return root * root == num

def generate_fibonacci_square_pairs(n):
    """
    Generate a Fibonacci-like sequence where the sum of consecutive pairs is a perfect square.
    
    Args:
        n (int): Number of elements to generate in the sequence
    
    Returns:
        list: A list of n numbers where consecutive pair sums are perfect squares
    
    Raises:
        ValueError: If n is less than 2
    """
    if n < 2:
        raise ValueError("n must be at least 2")
    
    # Initialize the sequence
    sequence = [1, 1]
    
    while len(sequence) < n:
        # Generate next number
        next_num = sequence[-1] + sequence[-2]
        
        # Check if the sum of last two pairs is a perfect square
        while not is_perfect_square(sequence[-1] + sequence[-2]):
            next_num += 1
        
        sequence.append(next_num)
    
    return sequence