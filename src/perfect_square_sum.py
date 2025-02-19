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
    
    # Check each number in the set
    for num in integer_set:
        # Check if the number itself is a perfect square
        sqrt_val = int(sqrt(num))
        if sqrt_val * sqrt_val == num:
            perfect_squares.add(num)
        
        # Try concatenating with other numbers
        for other in integer_set:
            # Concatenate and check
            concat_num = int(f"{num}{other}")
            sqrt_val = int(sqrt(concat_num))
            if sqrt_val * sqrt_val == concat_num:
                perfect_squares.add(concat_num)
    
    # Return the sum of unique perfect squares
    return sum(perfect_squares)