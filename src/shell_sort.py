def shell_sort(arr):
    """
    Implement the Shell sort algorithm to sort a list in-place.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Start with a large gap, then reduce gap
    n = len(arr)
    gap = n // 2
    
    # Do a gapped insertion sort for this gap size
    while gap > 0:
        # Perform gapped insertion sort for this gap size
        for i in range(gap, n):
            # Save arr[i] as the element to be compared
            temp = arr[i]
            
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Place temp (the original arr[i]) in its correct location
            arr[j] = temp
        
        # Reduce gap
        gap //= 2
    
    return arr