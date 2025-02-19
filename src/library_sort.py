def library_sort(arr):
    """
    Implement the library sort (patience sort) algorithm.
    
    Library sort is a sorting algorithm that works by creating multiple sorted 'piles'
    and then merging them, similar to how a librarian might sort books.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (similar to patience sort)
    piles = []
    
    for item in arr:
        # Find the correct pile to place the item
        placed = False
        for pile in piles:
            # If the item can be added to the end of a pile
            if not pile or item >= pile[-1]:
                pile.append(item)
                placed = True
                break
        
        # If no suitable pile is found, create a new pile
        if not placed:
            piles.append([item])
    
    # Merge the piles
    sorted_arr = []
    while piles:
        # Find the pile with the smallest top element
        min_pile_index = 0
        for i in range(1, len(piles)):
            if piles[i][0] < piles[min_pile_index][0]:
                min_pile_index = i
        
        # Add the smallest element to the sorted array
        sorted_arr.append(piles[min_pile_index].pop(0))
        
        # Remove empty piles
        if not piles[min_pile_index]:
            piles.pop(min_pile_index)
    
    return sorted_arr