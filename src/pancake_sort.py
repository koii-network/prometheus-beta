def pancake_sort(arr):
    """
    Implement the pancake sort algorithm.
    
    Pancake sort works by repeatedly flipping the largest unsorted element 
    to the beginning of the list and then flipping it to its correct position.
    
    Args:
        arr (list): The list to be sorted in ascending order
    
    Returns:
        list: The sorted list
    """
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Start from the last element and move towards the first
    for size in range(len(arr), 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = arr[:size].index(max(arr[:size]))
        
        # If the max element is not already at the end of the unsorted portion
        if max_idx != size - 1:
            # If the max element is not at the start, flip it to the start
            if max_idx != 0:
                arr[:max_idx+1] = arr[:max_idx+1][::-1]
            
            # Flip the max element to its correct position
            arr[:size] = arr[:size][::-1]
    
    return arr