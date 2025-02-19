import math

def generate_fibonacci_square_pairs(n):
    """
    Generate a Fibonacci-like sequence where consecutive pair sums are square numbers.
    
    Args:
        n (int): Number of elements to generate in the sequence
    
    Returns:
        list: A list of n numbers where consecutive pair sums are perfect squares
    
    Raises:
        ValueError: If n is less than 2
    """
    if n < 2:
        raise ValueError("Sequence length must be at least 2")
    
    # Initialize the sequence with first two terms
    sequence = [1, 1]
    
    while len(sequence) < n:
        # Generate next number such that sum of last two is a perfect square
        last = sequence[-1]
        second_last = sequence[-2]
        
        # Try next candidates
        for next_num in range(last + second_last, last + second_last + 100):
            # Check if the sum of the last two is a perfect square
            pair_sum = last + second_last
            sqrt_sum = math.isqrt(pair_sum)
            
            if sqrt_sum * sqrt_sum == pair_sum:
                sequence.append(next_num)
                break
        
        # Prevent infinite loop if no valid number is found
        if len(sequence) == n - 1:
            raise ValueError("Could not generate a sequence with square pair sums")
    
    return sequence