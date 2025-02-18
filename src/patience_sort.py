from typing import List, TypeVar, Callable
import heapq

T = TypeVar('T')

def patience_sort(arr: List[T], key: Callable[[T], float] = None) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Args:
        arr (List[T]): The input list to be sorted
        key (Callable[[T], float], optional): A function to extract a comparison key from each element. 
                                              Defaults to the identity function.
    
    Returns:
        List[T]: A new sorted list
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # If the input list is empty, return an empty list
    if not arr:
        return []
    
    # If no key function is provided, use the identity function
    if key is None:
        key = lambda x: x
    
    # Create piles (lists of elements)
    piles = []
    
    # Process each element in the input array
    for item in arr:
        # Create a new pile or place the item in an existing pile
        new_pile = [item]
        
        # Find the right pile to place the item
        placed = False
        for pile in piles:
            # Compare with the top of each pile
            if key(item) < key(pile[-1]):
                pile.append(item)
                placed = True
                break
        
        # If no suitable pile is found, create a new pile
        if not placed:
            piles.append(new_pile)
    
    # Merge piles using a min-heap
    result = []
    heap = []
    
    # Initialize the heap with the top element from each pile
    for i, pile in enumerate(piles):
        if pile:
            heapq.heappush(heap, (key(pile[0]), i, pile[0]))
    
    # Merge elements from piles
    while heap:
        _, pile_index, item = heapq.heappop(heap)
        result.append(item)
        
        # Remove the top element from the corresponding pile
        piles[pile_index].pop(0)
        
        # If the pile is not empty, add its next element to the heap
        if piles[pile_index]:
            heapq.heappush(heap, (key(piles[pile_index][0]), pile_index, piles[pile_index][0]))
    
    return result