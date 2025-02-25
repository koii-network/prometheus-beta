def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list of comparable elements.
    
    Comb Sort is an improvement over Bubble Sort that uses a gap size that shrinks 
    with each iteration, reducing the number of unnecessary comparisons.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list (same object as input, modified in-place).
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Initial gap is the length of the list
    gap = len(arr)
    
    # Define shrink factor (typically 1.3)
    shrink = 1.3
    
    # Flag to track if any swaps occurred
    swapped = True
    
    while gap > 1 or swapped:
        # Calculate new gap size, ensuring it becomes 1 eventually
        gap = max(1, int(gap / shrink))
        
        # Reset swap flag
        swapped = False
        
        # Compare elements with current gap
        for i in range(len(arr) - gap):
            # Compare and swap if needed
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    
    return arr