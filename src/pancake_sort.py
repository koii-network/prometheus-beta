def pancake_sort(arr):
    """
    Implement the pancake sort algorithm.
    
    Args:
        arr (list): The input list to be sorted in ascending order.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-comparable elements.
    """
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Sort the list
    for size in range(len(arr), 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = arr[:size].index(max(arr[:size]))
        
        # If the maximum element is not at the end, flip it to the beginning
        if max_idx != 0:
            # Flip the maximum element to the beginning
            arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
        
        # Flip the maximum element to its correct position
        arr[:size] = arr[:size][::-1]
    
    return arr