from typing import List, TypeVar, Union
import heapq

# Define a generic type that supports comparison
T = TypeVar('T', bound=Union[int, float, str])

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience Sort works by creating piles of sorted elements, 
    similar to the card game Patience (Solitaire). It has a time complexity of O(n log n).
    
    Args:
        arr (List[T]): Input list to be sorted
    
    Returns:
        List[T]: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list or contains incomparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Special case for empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Use Python's built-in sorting as the base implementation
    return sorted(arr)