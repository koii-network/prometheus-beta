from typing import List, Any

def library_sort(arr: List[Any]) -> List[Any]:
    """
    Implement the library sort (patience sorting) algorithm.
    
    Args:
        arr (List[Any]): The input list to be sorted
    
    Returns:
        List[Any]: A sorted list in ascending order
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not arr:
        return []
    
    # Create piles (like a card game)
    piles = []
    
    for item in arr:
        # Find the rightmost pile where we can place the item
        placed = False
        for pile in piles:
            if not pile or item < pile[-1]:
                pile.append(item)
                placed = True
                break
        
        # If no suitable pile found, create a new pile
        if not placed:
            piles.append([item])
    
    # Merge the piles
    result = []
    while piles:
        # Find the pile with the smallest top card
        smallest_pile_index = 0
        for i in range(1, len(piles)):
            if piles[i][0] < piles[smallest_pile_index][0]:
                smallest_pile_index = i
        
        # Pop the smallest item and add to result
        result.append(piles[smallest_pile_index].pop(0))
        
        # Remove empty piles
        if not piles[smallest_pile_index]:
            piles.pop(smallest_pile_index)
    
    return result