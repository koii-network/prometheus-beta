def insertion_sort(arr):
    """
    Implements the insertion sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Traverse through 1 to len(sorted_arr)
    for i in range(1, len(sorted_arr)):
        # Store the current element to be positioned
        key = sorted_arr[i]
        
        # Move elements of sorted_arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        
        # Place the key in its correct position
        sorted_arr[j + 1] = key
    
    return sorted_arr