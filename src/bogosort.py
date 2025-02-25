import random
from typing import List, TypeVar

T = TypeVar('T')

def bogosort(arr: List[T]) -> List[T]:
    """
    Implement the bogosort (permutation sort) algorithm.
    
    Bogosort is an extremely inefficient sorting algorithm that works by 
    randomly shuffling the input list until it happens to be sorted.
    
    Args:
        arr (List[T]): The input list to be sorted.
    
    Returns:
        List[T]: A sorted version of the input list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    
    Note:
        This algorithm has an average and worst-case time complexity of O(∞).
        It is NOT recommended for practical use and is purely for educational purposes.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Helper function to check if list is sorted
    def is_sorted(lst: List[T]) -> bool:
        return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))
    
    # Create a copy to avoid modifying the original list
    working_list = arr.copy()
    
    # Keep shuffling until sorted
    while not is_sorted(working_list):
        random.shuffle(working_list)
    
    return working_list