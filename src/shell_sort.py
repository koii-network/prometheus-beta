def shell_sort(arr):
    """
    Implement the Shell Sort algorithm to sort a list of elements.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    
    # Initialize the gap sequence
    n = len(arr)
    gap = n // 2
    
    # Reduce gap in each iteration
    while gap > 0:
        # Do a gapped insertion sort for this gap size
        for i in range(gap, n):
            # Save the current element to be compared
            temp = arr[i]
            
            # Shift earlier gap-sorted elements up until the correct location for temp is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Place temp in its correct location
            arr[j] = temp
        
        # Reduce the gap for next iteration
        gap //= 2
    
    return arr