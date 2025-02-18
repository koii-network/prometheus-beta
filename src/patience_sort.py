from typing import List, TypeVar, Comparable

T = TypeVar('T', bound=Comparable)

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience sort is an algorithm that sorts a list by simulating a card sorting process.
    It works by creating piles (like in the game of Patience/Solitaire) and then merging them.
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A new sorted list
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (each pile represents a sorted subsequence)
    piles = []
    
    for item in arr:
        # Try to place the item on an existing pile
        placed = False
        for pile in piles:
            # If the item is less than or equal to the top of the pile, 
            # add it to that pile
            if not pile or item <= pile[-1]:
                pile.append(item)
                placed = True
                break
        
        # If no suitable pile is found, create a new pile
        if not placed:
            piles.append([item])
    
    # Merge piles using a min-heap approach
    result = []
    heap = [(pile[-1], i) for i, pile in enumerate(piles)]
    heap.sort()  # Convert to a sorted list acting as a min-heap
    
    while heap:
        # Get the smallest top item
        val, pile_index = heap.pop(0)
        result.append(val)
        
        # Remove the top item from its pile
        piles[pile_index].pop()
        
        # If the pile is not empty, add its new top item to the heap
        if piles[pile_index]:
            new_top = piles[pile_index][-1]
            # Insert in sorted position
            insert_index = 0
            while insert_index < len(heap) and heap[insert_index][0] < new_top:
                insert_index += 1
            heap.insert(insert_index, (new_top, pile_index))
    
    return result