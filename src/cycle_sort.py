def cycle_sort(arr):
    """
    Implement the Cycle Sort algorithm.
    
    Cycle sort is an in-place, unstable sorting algorithm that is optimal in terms 
    of the number of memory writes. It works by minimizing the number of memory writes 
    to sort an array.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list (same object as input, modified in-place).
    
    Raises:
        TypeError: If the input is not a list or contains unhashable elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list or list with single element
    n = len(arr)
    if n <= 1:
        return arr
    
    # Perform cycle sort
    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        
        # Find where to put the item
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        
        # If item is already in correct position
        if pos == cycle_start:
            continue
        
        # Otherwise, put the item there or right after any duplicates
        while item == arr[pos]:
            pos += 1
        
        # Swap the items
        arr[pos], item = item, arr[pos]
        
        # Rotate the rest of the cycle
        while pos != cycle_start:
            # Find where to put the item
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            
            # Place the item
            while item == arr[pos]:
                pos += 1
            
            # Swap
            arr[pos], item = item, arr[pos]
    
    return arr