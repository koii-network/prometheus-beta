def pancake_sort(arr):
    """
    Implement the pancake sort algorithm.
    
    Pancake sort works by flipping the largest unsorted element to the top 
    and then flipping the entire sorted portion to the bottom in each iteration.
    
    Args:
        arr (list): The list to be sorted in ascending order
    
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
    arr = arr.copy()
    
    # Get the length of the list
    n = len(arr)
    
    # Traverse through all array elements
    for curr_size in range(n, 1, -1):
        # Find index of the maximum element in the unsorted portion
        max_index = arr[:curr_size].index(max(arr[:curr_size]))
        
        # If the maximum is not already at the end, flip it to the top
        if max_index != 0:
            # Flip the maximum to the top
            arr[:max_index+1] = arr[:max_index+1][::-1]
        
        # Flip the entire unsorted portion to put max at the bottom
        arr[:curr_size] = arr[:curr_size][::-1]
    
    return arr