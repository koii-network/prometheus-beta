from typing import List, Any
import heapq

def patience_sort(arr: List[Any]) -> List[Any]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience sort is a sorting algorithm inspired by the card game patience (solitaire).
    It works by creating a series of piles and then merging them efficiently.
    
    Args:
        arr (List[Any]): The input list to be sorted
    
    Returns:
        List[Any]: A sorted list in ascending order
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (stacks) 
    piles = []
    
    # Place each element in a pile
    for item in arr:
        # Find the rightmost pile where we can place the item
        found_pile = False
        for pile in piles:
            # If the pile is empty or the item is less than or equal to the top of the pile
            if not pile or item <= pile[-1]:
                pile.append(item)
                found_pile = True
                break
        
        # If no suitable pile is found, create a new pile
        if not found_pile:
            piles.append([item])
    
    # Merge piles using a min-heap
    result = []
    heap = [(pile[-1], i, pile) for i, pile in enumerate(piles)]
    heapq.heapify(heap)
    
    while heap:
        val, pile_index, pile = heapq.heappop(heap)
        result.append(val)
        pile.pop()
        
        # If the pile is not empty, add its top element back to the heap
        if pile:
            heapq.heappush(heap, (pile[-1], pile_index, pile))
    
    return result