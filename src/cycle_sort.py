def cycle_sort(arr):
    """
    Implement the Cycle Sort algorithm to sort an array in-place.
    
    Cycle sort is an in-place, unstable sorting algorithm that is optimal in terms 
    of the number of memory writes. It works well for arrays with many duplicate elements.
    
    Args:
        arr (list): The input list to be sorted in-place
    
    Returns:
        list: The sorted list (same object as input, modified in-place)
    
    Raises:
        TypeError: If the input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Get the length of the array
    n = len(arr)
    
    # Traverse through all array elements
    for cycle_start in range(n - 1):
        # Find the item to put in the correct position 
        item = arr[cycle_start]
        
        # Find the position where we put the item 
        pos = cycle_start 
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        
        # If the item is already in the correct position 
        if pos == cycle_start:
            continue
        
        # Otherwise, put the item there or right after any duplicates 
        while item == arr[pos]:
            pos += 1
        
        # Swap the item with the element at the calculated position
        arr[pos], item = item, arr[pos]
        
        # Rotate the rest of the cycle 
        while pos != cycle_start:
            # Find the position where we put the item 
            pos = cycle_start 
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            
            # Move the item to its correct position
            while item == arr[pos]:
                pos += 1
            
            # Swap 
            arr[pos], item = item, arr[pos]
    
    return arr