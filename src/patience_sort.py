from typing import List, TypeVar, Union

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
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (stacks)
    piles = []
    
    # Distribute elements into piles
    for item in arr:
        # Find the rightmost pile where we can place the item
        inserted = False
        for pile in piles:
            # If the current pile's top is greater, we can place the item
            if not pile or item <= pile[-1]:
                pile.append(item)
                inserted = True
                break
        
        # If no existing pile works, create a new pile
        if not inserted:
            piles.append([item])
    
    # Merge piles using a min-heap like approach
    result = []
    while piles:
        # Find the pile with the smallest top element
        min_pile_index = 0
        for i in range(1, len(piles)):
            if piles[i][0] < piles[min_pile_index][0]:
                min_pile_index = i
        
        # Pop and add the smallest element
        result.append(piles[min_pile_index].pop(0))
        
        # Remove the pile if it becomes empty
        if not piles[min_pile_index]:
            piles.pop(min_pile_index)
    
    return result