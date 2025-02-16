def library_sort(arr):
    """
    Implement the library sort (or patience sort) algorithm.
    
    Library sort works by maintaining multiple sorted 'piles' of elements,
    with the goal of achieving an overall sorted result with O(n log n) complexity.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list containing all elements from the input
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (initial list of lists)
    piles = []
    
    for item in arr:
        # Find the correct pile to place the current item
        inserted = False
        for pile in piles:
            # If the item can be inserted at the end of a pile
            if not pile or item >= pile[-1]:
                pile.append(item)
                inserted = True
                break
        
        # If no suitable pile was found, create a new pile
        if not inserted:
            piles.append([item])
    
    # Merge the piles
    result = []
    while piles:
        # Find the pile with the smallest top element
        min_pile_index = 0
        for i in range(1, len(piles)):
            if piles[i][0] < piles[min_pile_index][0]:
                min_pile_index = i
        
        # Remove and add the smallest element
        result.append(piles[min_pile_index].pop(0))
        
        # Remove empty piles
        if not piles[min_pile_index]:
            piles.pop(min_pile_index)
    
    return result