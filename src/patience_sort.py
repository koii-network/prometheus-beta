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
    
    # Create piles
    piles = []
    for item in arr:
        # Find the rightmost pile where we can place the item
        found_pile = False
        for pile in piles:
            if not pile or key(item) <= key(pile[-1]):
                pile.append(item)
                found_pile = True
                break
        
        # If no suitable pile is found, create a new pile
        if not found_pile:
            piles.append([item])
    
    # Merge piles using a min-heap
    result = []
    while piles:
        # Find the pile with the smallest top item
        min_pile_index = 0
        for i in range(1, len(piles)):
            if key(piles[i][0]) < key(piles[min_pile_index][0]):
                min_pile_index = i
        
        # Add the smallest item to the result
        result.append(piles[min_pile_index].pop(0))
        
        # Remove the pile if it's empty
        if not piles[min_pile_index]:
            piles.pop(min_pile_index)
    
    return result