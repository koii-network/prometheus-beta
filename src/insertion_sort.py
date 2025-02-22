def insertion_sort(arr):
    """
    Implement the insertion sort algorithm.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains incomparable elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Insertion sort algorithm
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        
        # Move elements of sorted_arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        
        sorted_arr[j + 1] = key
    
    return sorted_arr