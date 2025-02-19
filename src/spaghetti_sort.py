def spaghetti_sort(arr):
    """
    Implement the spaghetti sort algorithm.
    
    The spaghetti sort (also known as patience sorting) works by:
    1. Creating multiple 'piles' 
    2. Placing each element in the first pile where it can go
    3. Collecting elements from the piles in order
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles
    piles = []
    for item in arr:
        # Find the first pile where this item can be placed
        placed = False
        for pile in piles:
            if not pile or item >= pile[-1]:
                pile.append(item)
                placed = True
                break
        
        # If no existing pile works, create a new pile
        if not placed:
            piles.append([item])
    
    # Collect and merge piles
    result = []
    while piles:
        # Find the pile with the smallest top element
        min_pile_index = 0
        for i in range(1, len(piles)):
            if piles[i][0] < piles[min_pile_index][0]:
                min_pile_index = i
        
        # Add the top element to result and remove it from its pile
        result.append(piles[min_pile_index].pop(0))
        
        # Remove empty piles
        if not piles[min_pile_index]:
            piles.pop(min_pile_index)
    
    return result