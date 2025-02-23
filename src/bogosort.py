import random
from typing import List, TypeVar

T = TypeVar('T')

def bogosort(arr: List[T]) -> List[T]:
    """
    Implement the bogosort (permutation sort) algorithm.
    
    Bogosort is an extremely inefficient sorting algorithm that works by 
    randomly shuffling the list until it becomes sorted. 
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A sorted version of the input list
    
    Raises:
        TypeError: If the input is not a list
    
    Note:
        Time complexity: O(∞) - theoretically unbounded
        This is more of a joke/educational algorithm than a practical sorting method
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Shuffle and check if sorted
    while not is_sorted(arr):
        random.shuffle(arr)
    
    return arr

def is_sorted(arr: List[T]) -> bool:
    """
    Check if a list is sorted in ascending order.
    
    Args:
        arr (List[T]): The list to check for sortedness
    
    Returns:
        bool: True if the list is sorted, False otherwise
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))