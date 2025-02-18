def insertion_sort(arr):
    """
    Implement the insertion sort algorithm to sort a list in-place.
    
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
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        key = arr[i]
        
        # Move elements of arr[0..i-1] that are greater than key 
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key
    
    return arr