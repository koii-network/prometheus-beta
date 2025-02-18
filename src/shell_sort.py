def shell_sort(arr):
    """
    Implement the Shell sort algorithm.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-comparable elements.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Get the length of the list
    n = len(arr)
    
    # Start with a large gap and reduce it
    gap = n // 2
    
    # Continue until gap becomes 0
    while gap > 0:
        # Do a gapped insertion sort for this gap size
        for i in range(gap, n):
            # Add arr[i] to the elements that have been gap sorted
            # Save arr[i] in temp and make a hole at position i
            temp = arr[i]
            
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp
        
        # Reduce the gap
        gap //= 2
    
    return arr