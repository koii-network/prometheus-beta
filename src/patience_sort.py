from typing import List, TypeVar, Comparable
import heapq

T = TypeVar('T', bound=Comparable)

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    The algorithm works by creating piles of cards (sublists) and then merging them.
    Time complexity: O(n log n)
    Space complexity: O(n)
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A new sorted list
    """
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (sublists)
    piles = []
    for item in arr:
        # Try to place the item on an existing pile
        placed = False
        for pile in piles:
            if not pile or item >= pile[-1]:
                pile.append(item)
                placed = True
                break
        
        # If no suitable pile found, create a new pile
        if not placed:
            piles.append([item])
    
    # Merge piles using a min-heap
    result = []
    heap = [(pile[0], i, pile) for i, pile in enumerate(piles)]
    heapq.heapify(heap)
    
    while heap:
        val, pile_index, pile = heapq.heappop(heap)
        result.append(val)
        
        # Remove the used item from its pile
        pile.pop(0)
        
        # If the pile is not empty, add the next item to the heap
        if pile:
            heapq.heappush(heap, (pile[0], pile_index, pile))
    
    return result