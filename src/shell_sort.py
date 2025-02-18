def shell_sort(arr):
    """
    Implement the Shell sort algorithm.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If input is not a list.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    n = len(arr)
    
    # Start with a large gap, then reduce gap
    gap = n // 2
    
    # Do a gapped insertion sort for this gap size
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array 
    # is gap sorted
    while gap > 0:
        
        # Do gapped insertion sort for this gap size. 
        # The first gap elements a[0..gap-1] are already in gapped
        # order keep adding one more element until the entire array
        # is gap sorted
        for i in range(gap, n):
            
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
            
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        
        # Reduce gap 
        gap //= 2
    
    return arr