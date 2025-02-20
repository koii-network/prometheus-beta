from typing import List, Tuple

def separate_evens_odds(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Separate the input list of numbers into two lists: even and odd numbers.
    
    Args:
        numbers (List[int]): Input list of integers
    
    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists 
        - first list with even numbers, 
        - second list with odd numbers
    """
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    return (evens, odds)