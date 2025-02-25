from typing import Set, Union
import math

def sum_perfect_squares_from_set(numbers: Set[int]) -> int:
    """
    Calculate the sum of all perfect squares that can be formed from integers in the given set.
    
    Args:
        numbers (Set[int]): A set of integers to check for perfect square combinations.
    
    Returns:
        int: The sum of all unique perfect squares that can be formed from the set.
    
    Raises:
        TypeError: If the input is not a set of integers.
        ValueError: If any number in the set is negative.
    
    Examples:
        >>> sum_perfect_squares_from_set({1, 2, 3})  # 1^2 + 2^2 = 5
        5
        >>> sum_perfect_squares_from_set({4, 9})  # 2^2 + 3^2 = 13
        13
    """
    # Validate input
    if not isinstance(numbers, set):
        raise TypeError("Input must be a set of integers")
    
    # Check for non-integer or negative values
    if not all(isinstance(num, int) and num >= 0 for num in numbers):
        raise ValueError("Set must contain only non-negative integers")
    
    # Find all unique perfect squares
    perfect_squares = set()
    
    # Check each number and their combinations
    for i in range(len(list(numbers))):
        num = list(numbers)[i]
        # Check if the number itself is a perfect square
        if math.isqrt(num) ** 2 == num:
            perfect_squares.add(num)
        
        # Check with other numbers 
        for j in range(i+1, len(list(numbers))):
            other = list(numbers)[j]
            
            # Check combined products 
            combined = num * other
            if math.isqrt(combined) ** 2 == combined:
                perfect_squares.add(combined)
    
    # Return the sum of unique perfect squares
    return sum(perfect_squares)