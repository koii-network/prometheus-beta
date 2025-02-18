def cycle_sort(arr):
    """
    Implement the Cycle Sort algorithm.
    
    Cycle sort is an in-place, unstable sorting algorithm that minimizes the number 
    of memory writes by finding the correct position for each element before placing it.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list (same object as input, modified in-place).
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Traverse through all array elements
    for cycle_start in range(len(arr) - 1):
        item = arr[cycle_start]
        
        # Find where to put the item
        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < item:
                pos += 1
        
        # If the item is already in the correct position
        if pos == cycle_start:
            continue
        
        # Otherwise, put the item there or right after any duplicates
        while item == arr[pos]:
            pos += 1
        
        # Swap the items
        arr[pos], item = item, arr[pos]
        
        # Rotate the rest of the cycle
        while pos != cycle_start:
            # Find the position for the current item 
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < item:
                    pos += 1
            
            # Ignore all duplicate elements
            while item == arr[pos]:
                pos += 1
            
            # Put the item to its right position
            arr[pos], item = item, arr[pos]
    
    return arr