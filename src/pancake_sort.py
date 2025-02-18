def pancake_sort(arr):
    """
    Implement the pancake sort algorithm.
    
    Pancake sort works by flipping sublists to sort the entire list.
    Time complexity: O(n^2)
    Space complexity: O(1)
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list in ascending order
    """
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Traverse through all array elements
    for curr_size in range(len(arr), 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = arr.index(max(arr[:curr_size]))
        
        # If the max element is not at the end of the current sublist
        if max_idx != curr_size - 1:
            # If the max element is not at the beginning, flip it to the start
            if max_idx != 0:
                # Flip to bring the maximum to the start
                arr[:max_idx+1] = arr[:max_idx+1][::-1]
            
            # Flip the entire current sublist to bring max to its correct position
            arr[:curr_size] = arr[:curr_size][::-1]
    
    return arr