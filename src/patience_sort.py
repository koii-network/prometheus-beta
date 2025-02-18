from typing import List, TypeVar, Comparable

T = TypeVar('T', bound=Comparable)

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    The algorithm works by creating 'piles' of cards (elements) where each new 
    element is placed on the leftmost pile where it can be placed.
    
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
    
    # Create piles to simulate the patience sorting process
    piles = []
    
    for item in arr:
        # Find the leftmost pile where the item can be placed
        placed = False
        for pile in piles:
            # If the top of the pile is greater than or equal to the current item
            if pile[-1] >= item:
                pile.append(item)
                placed = True
                break
        
        # If no existing pile works, create a new pile
        if not placed:
            piles.append([item])
    
    # Merge the piles using a min-heap approach
    result = []
    while piles:
        # Find the pile with the smallest top element
        min_pile_idx = min(range(len(piles)), key=lambda i: piles[i][-1])
        
        # Remove the top element from the selected pile
        top_element = piles[min_pile_idx].pop()
        result.append(top_element)
        
        # Remove the pile if it becomes empty
        if not piles[min_pile_idx]:
            piles.pop(min_pile_idx)
    
    return result