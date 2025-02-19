from itertools import combinations
from math import sqrt

def sum_perfect_squares_from_set(integer_set):
    """
    Calculates the sum of all unique perfect squares that can be formed 
    from the integers in the given set.
    
    Args:
        integer_set (set): A set of integers
    
    Returns:
        int: Sum of all unique perfect squares formable from the set
    """
    # Validate input is a set of integers
    if not isinstance(integer_set, set):
        raise TypeError("Input must be a set")
    
    if not all(isinstance(x, int) for x in integer_set):
        raise TypeError("Set must contain only integers")
    
    # Find all possible perfect squares
    perfect_squares = set()
    
    # Try all possible combinations of numbers in the set
    for r in range(1, len(integer_set) + 1):
        for combo in combinations(integer_set, r):
            # Convert combination to a number
            num = int(''.join(map(str, combo)))
            
            # Check if the number is a perfect square
            if num > 0:
                sqrt_val = int(sqrt(num))
                if sqrt_val * sqrt_val == num:
                    perfect_squares.add(num)
    
    # Return the sum of unique perfect squares
    return sum(perfect_squares)