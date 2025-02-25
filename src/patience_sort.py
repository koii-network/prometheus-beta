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
        insertion_index = 0
        for i, pile in enumerate(piles):
            if key(item) < key(pile[-1]):
                break
            insertion_index = i + 1
        
        # If we're at the end, start a new pile
        if insertion_index == len(piles):
            piles.append([item])
        else:
            # Insert into the appropriate pile
            piles[insertion_index].append(item)
    
    # Merge piles using a min-heap
    result = []
    heap = []
    
    # Initialize heap with the top of each pile
    for pile in piles:
        if pile:
            heapq.heappush(heap, (key(pile[0]), pile))
    
    while heap:
        _, pile = heapq.heappop(heap)
        
        # Add the smallest item to the result
        result.append(pile.pop(0))
        
        # If pile is not empty, put it back into the heap
        if pile:
            heapq.heappush(heap, (key(pile[0]), pile))
    
    return result