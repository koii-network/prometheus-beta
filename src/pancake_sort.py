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
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Check if all elements are comparable
    try:
        arr.sort()
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    # Pancake sort implementation
    def flip(arr, k):
        """Reverse the first k elements of the list."""
        return arr[:k][::-1] + arr[k:]
    
    # Sort the list using pancake flipping
    for size in range(len(arr), 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = arr[:size].index(max(arr[:size]))
        
        # If the max element is not at the end of the unsorted portion
        if max_idx != size - 1:
            # If max element is not at the beginning, flip to bring it to the start
            if max_idx != 0:
                arr = flip(arr, max_idx + 1)
            
            # Flip to move the max element to its correct position
            arr = flip(arr, size)
    
    return arr