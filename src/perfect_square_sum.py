import math

def sum_perfect_squares(number_set):
    """
    Accepts a set of integers and returns the sum of all perfect squares that can be formed 
    from the integers in the set.
    
    Args:
        number_set (set): A set of integers
    
    Returns:
        int: Sum of all unique perfect squares that can be formed from the input set
    """
    # Validate input is a set
    if not isinstance(number_set, set):
        raise TypeError("Input must be a set of integers")
    
    # Filter out non-integers and negative numbers
    valid_numbers = {num for num in number_set if isinstance(num, int) and num >= 0}
    
    # Find all possible perfect squares
    perfect_squares = set()
    for num in valid_numbers:
        for other_num in valid_numbers:
            square = num * other_num
            if math.isqrt(square) ** 2 == square:
                perfect_squares.add(square)
    
    return sum(perfect_squares)