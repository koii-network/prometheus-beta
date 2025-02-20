def bubble_sort(arr):
    """
    Perform bubble sort with optimization to reduce unnecessary swapping.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list.
    """
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr
    
    # Create a copy to avoid modifying the original list
    result = arr.copy()
    n = len(result)
    
    # Iterate through the list
    for i in range(n):
        # Flag to track if any swaps occurred in this pass
        swapped = False
        
        # Last i elements are already in place, so reduce the inner loop range
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if result[j] > result[j + 1]:
                # Swap elements
                result[j], result[j + 1] = result[j + 1], result[j]
                # Set swapped flag to True
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return result