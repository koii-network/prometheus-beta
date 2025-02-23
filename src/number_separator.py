from typing import List, Tuple

def separate_evens_odds(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Separate a list of integers into even and odd lists.
    
    Args:
        numbers: A list of integers to be separated
    
    Returns:
        A tuple containing two lists: 
        - First list contains even numbers 
        - Second list contains odd numbers
    """
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    return (evens, odds)