from typing import List, Tuple

def separate_evens_odds(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Separate a list of integers into two lists: one with even numbers and one with odd numbers.
    
    Args:
        numbers (List[int]): Input list of integers to be separated
    
    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists 
        - First list: even numbers 
        - Second list: odd numbers
    
    Examples:
        >>> separate_evens_odds([1, 2, 3, 4, 5])
        ([2, 4], [1, 3, 5])
        >>> separate_evens_odds([])
        ([], [])
    """
    # Handle empty list case
    if not numbers:
        return [], []
    
    # Use list comprehensions to separate even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    return even_numbers, odd_numbers