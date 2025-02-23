import random
from typing import List, TypeVar

T = TypeVar('T')

def bogosort(arr: List[T]) -> List[T]:
    """
    Implement the bogosort (permutation sort) algorithm.
    
    Bogosort is an extremely inefficient sorting algorithm that works by randomly 
    shuffling the list until it becomes sorted. It has an average and worst-case 
    time complexity of O(∞), making it unsuitable for practical use.
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A sorted version of the input list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Special cases for empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Helper function to check if list is sorted
    def is_sorted(lst: List[T]) -> bool:
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Deep copy to avoid modifying original list
    working_list = arr.copy()
    
    # Keep shuffling until sorted
    while not is_sorted(working_list):
        random.shuffle(working_list)
    
    return working_list