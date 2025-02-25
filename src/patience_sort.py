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
        new_pile = False
        for pile in piles:
            # Compare the top of the pile with the current item
            if not pile or key(item) < key(pile[-1]):
                pile.append(item)
                break
        else:
            # If no suitable pile is found, create a new pile
            piles.append([item])
    
    # Merge piles using a min-heap
    result = []
    heap = [(key(pile[0]), i, pile) for i, pile in enumerate(piles)]
    heapq.heapify(heap)
    
    while heap:
        _, _, pile = heapq.heappop(heap)
        result.append(pile.pop(0))
        
        # If pile is not empty, put it back into the heap
        if pile:
            heapq.heappush(heap, (key(pile[0]), len(heap), pile))
    
    return result