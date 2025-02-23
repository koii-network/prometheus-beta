def pancake_sort(arr):
    """
    Implement the pancake sort algorithm to sort a list in ascending order.
    
    The pancake sort algorithm works by flipping subarrays to sort the list.
    It repeatedly finds the maximum element and flips it to the beginning,
    then flips it to its correct position.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        TypeError: If the list contains elements that cannot be compared
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Perform pancake sort
    for size in range(len(sorted_arr), 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = sorted_arr[:size].index(max(sorted_arr[:size]))
        
        # If max element is not at the end, flip it to the beginning and then to its correct position
        if max_idx != size - 1:
            # Flip to bring max to the front
            if max_idx != 0:
                sorted_arr[:max_idx+1] = sorted_arr[:max_idx+1][::-1]
            
            # Flip to put max at its correct position
            sorted_arr[:size] = sorted_arr[:size][::-1]
    
    return sorted_arr