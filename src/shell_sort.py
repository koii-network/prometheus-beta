def shell_sort(arr):
    """
    Implement the Shell Sort algorithm for sorting a list of comparable elements.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Create a copy of the input list to avoid modifying the original
    arr = list(arr)
    
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Get the length of the list
    n = len(arr)
    
    # Start with a large gap, then reduce gap
    gap = n // 2
    
    # Do a gapped insertion sort for this gap size
    # The first gap elements a[0..gap-1] are already in gapped order
    # Keep adding one more element until the entire array is gap sorted
    while gap > 0:
        # Do gapped insertion sort for this gap size
        # The first gap elements a[0..gap-1] are already in gapped order
        # Keep adding one more element until the entire array is gap sorted
        for i in range(gap, n):
            # Add a[i] to the elements that have been gap sorted
            # Save a[i] in temp and make a hole at position i
            temp = arr[i]
            
            # Shift earlier gap-sorted elements up until the correct location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Put temp (the original a[i]) in its correct location
            arr[j] = temp
        
        # Reduce the gap
        gap //= 2
    
    return arr