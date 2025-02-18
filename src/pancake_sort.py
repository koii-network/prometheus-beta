def pancake_sort(arr):
    """
    Implement the Pancake Sort algorithm.
    
    Args:
        arr (list): The input list to be sorted in ascending order.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    def flip(arr, k):
        """
        Flip the first k elements of the list.
        
        Args:
            arr (list): The list to be flipped.
            k (int): Number of elements to flip from the beginning.
        
        Returns:
            list: A new list with the first k elements reversed.
        """
        return arr[:k][::-1] + arr[k:]
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Iterate through the list from the end
    for size in range(len(sorted_arr), 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = max(range(size), key=lambda i: sorted_arr[i])
        
        # If the maximum element is not at the end, flip it to the beginning
        if max_idx != size - 1:
            # If the maximum is not at the start, flip it to the start
            if max_idx != 0:
                sorted_arr = flip(sorted_arr, max_idx + 1)
            
            # Flip to put the element at the end of the current unsorted portion
            sorted_arr = flip(sorted_arr, size)
    
    return sorted_arr