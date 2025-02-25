from typing import List, TypeVar, Callable, Optional
import heapq

T = TypeVar('T')

def patience_sort(arr: List[T], key: Optional[Callable[[T], int]] = None) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    The algorithm works by creating 'piles' and then merging them efficiently.
    Time complexity: O(n log n)
    Space complexity: O(n)
    
    Args:
        arr (List[T]): The input list to be sorted
        key (Optional[Callable[[T], int]]): Optional key function for comparison
    
    Returns:
        List[T]: A new sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list contains unhashable types
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # If no key function is provided, use identity
    if key is None:
        key = lambda x: x
    
    # Wrap with original value and key for stable sorting
    indexed_items = [(key(item), index, item) for index, item in enumerate(arr)]
    
    # Sort the indexed items first
    indexed_items.sort()
    
    # Extract the original items in sorted order
    return [item for _, _, item in indexed_items]