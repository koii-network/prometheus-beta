from typing import List, TypeVar, Any

T = TypeVar('T')

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience Sort is a sorting algorithm that works by creating a series of piles 
    and then merging them, similar to the card game Patience (Solitaire).
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check input type
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
        placed = False
        for pile in piles:
            # If the top of the pile is greater than the current item
            if not pile or item <= pile[-1]:
                pile.append(item)
                placed = True
                break
        
        # If no suitable pile is found, create a new pile
        if not placed:
            piles.append([item])
    
    # Merge piles
    result = []
    while piles:
        # Find the pile with the smallest top element
        smallest_pile_index = min(range(len(piles)), key=lambda i: piles[i][-1])
        
        # Remove and add the top element of the chosen pile
        result.append(piles[smallest_pile_index].pop())
        
        # Remove the pile if it becomes empty
        if not piles[smallest_pile_index]:
            piles.pop(smallest_pile_index)
    
    return result