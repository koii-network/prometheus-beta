def pancake_sort(arr):
    """
    Implement the pancake sort algorithm.
    
    Pancake sort works by flipping prefixes of the list to sort the entire array.
    The algorithm works as follows:
    1. Find the index of the maximum element in the unsorted portion
    2. Flip the subarray to bring the maximum element to the beginning
    3. Flip the entire unsorted portion to bring the maximum element to its correct position
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-comparable elements
    """
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    def flip(subarray, k):
        """
        Reverse the first k elements of the list
        
        Args:
            subarray (list): The list to be partially reversed
            k (int): Number of elements to reverse from the start
        
        Returns:
            list: List with first k elements reversed
        """
        return subarray[:k][::-1] + subarray[k:]
    
    # Main pancake sort logic
    for size in range(len(arr), 1, -1):
        # Find index of maximum element in unsorted portion
        max_idx = arr[:size].index(max(arr[:size]))
        
        # If max element is not at the end, do pancake flips
        if max_idx != size - 1:
            # First flip to bring max to the beginning
            if max_idx != 0:
                arr = flip(arr, max_idx + 1)
            
            # Then flip to bring max to its correct position
            arr = flip(arr, size)
    
    return arr