from typing import List, Tuple

def separate_evens_odds(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Separate a list of integers into even and odd numbers.
    
    Args:
        numbers (List[int]): Input list of integers
    
    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists 
        - first list with even numbers, 
        - second list with odd numbers
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    return even_numbers, odd_numbers