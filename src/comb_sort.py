def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list in ascending order.
    
    Comb Sort is an improvement over Bubble Sort. It starts with a large gap 
    and reduces the gap in each iteration, allowing faster movement of items 
    to their correct positions.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    
    # If list is empty or has only one element, return it as-is
    if len(arr) <= 1:
        return arr
    
    # Initial gap (shrink factor of 1.3 is commonly used)
    gap = len(arr)
    shrink = 1.3
    
    # Flag to check if any swaps occurred
    swapped = True
    
    while gap > 1 or swapped:
        # Calculate gap, ensure it's at least 1
        gap = max(1, int(gap / shrink))
        
        # Reset swapped flag
        swapped = False
        
        # Compare elements with current gap
        for i in range(len(arr) - gap):
            # If elements are out of order, swap them
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    
    return arr