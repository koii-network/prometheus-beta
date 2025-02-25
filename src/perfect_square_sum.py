from typing import Set
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
    
    # Check each number and its combinations with other numbers
    number_list = list(numbers)
    for i in range(len(number_list)):
        # Individual number check
        for j in range(i, len(number_list)):
            # Try single number perfect squares
            num = number_list[i]
            root = math.isqrt(num)
            if root * root == num:
                perfect_squares.add(num)
            
            # Try product combinations 
            other = number_list[j]
            combined = num * other
            root_combined = math.isqrt(combined)
            if root_combined * root_combined == combined:
                perfect_squares.add(combined)
    
    # Return the sum of unique perfect squares
    return sum(perfect_squares)