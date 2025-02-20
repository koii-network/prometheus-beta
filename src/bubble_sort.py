def optimized_bubble_sort(arr):
    """
    Perform an optimized bubble sort on the input list.
    
    The optimization uses a 'swapped' flag to detect if the list is already sorted,
    allowing early termination if no swaps are made in a full pass.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, it's already sorted
    n = len(arr)
    if n <= 1:
        return arr
    
    # Iterate through the list
    for i in range(n):
        # Assume no swaps will be needed (list might already be sorted)
        swapped = False
        
        # Last i elements are already in place, so reduce the inner loop
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set swapped flag to True
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return arr