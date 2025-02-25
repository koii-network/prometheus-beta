from typing import List, Tuple

def separate_evens_odds(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Separates a list of integers into two lists: even numbers and odd numbers.

    Args:
        numbers (List[int]): A list of integers to be separated.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists:
            - First list: even numbers
            - Second list: odd numbers

    Examples:
        >>> separate_evens_odds([1, 2, 3, 4, 5, 6])
        ([2, 4, 6], [1, 3, 5])
        >>> separate_evens_odds([])
        ([], [])
    """
    # Handle empty list case
    if not numbers:
        return [], []
    
    # Use list comprehensions to separate even and odd numbers
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    
    return evens, odds