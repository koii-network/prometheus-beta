def bubble_sort(arr):
    """
    Perform bubble sort on the input list with an optimization to reduce unnecessary swaps.
    
    The algorithm uses a `swapped` flag to track if any swaps were made during an iteration.
    If no swaps are made in a complete pass, the list is already sorted, and the algorithm 
    can terminate early.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list (same object as input, modified in-place).
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, it's already sorted
    n = len(arr)
    if n <= 1:
        return arr
    
    # Outer loop for passes
    for i in range(n):
        # Optimization: Assume list is sorted at the start of each pass
        swapped = False
        
        # Inner loop for comparisons and potential swaps
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Mark that a swap occurred
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return arr