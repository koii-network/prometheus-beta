def pancake_sort(arr):
    """
    Implement the pancake sort algorithm.
    
    Pancake sort works by flipping subarrays to sort the entire array.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Main pancake sort algorithm
    def flip(sublist, k):
        """Reverse the first k elements of the list"""
        left = 0
        while left < k:
            sublist[left], sublist[k] = sublist[k], sublist[left]
            left += 1
            k -= 1
        return sublist
    
    # Iterate through the list
    for curr_size in range(len(sorted_arr), 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = sorted_arr.index(max(sorted_arr[:curr_size]))
        
        # If the max is not at the end of the unsorted portion, flip
        if max_idx != curr_size - 1:
            # If max is not at the beginning, first flip to bring it to the start
            if max_idx != 0:
                sorted_arr = flip(sorted_arr, max_idx)
            
            # Then flip to put max at the end of current unsorted portion
            sorted_arr = flip(sorted_arr, curr_size - 1)
    
    return sorted_arr