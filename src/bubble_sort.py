def optimize_bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    This implementation includes two key optimizations:
    1. Early stopping when no swaps occur in a pass
    2. Reducing the number of iterations in subsequent passes
    
    Args:
        arr (list): The input list to be sorted in-place
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    n = len(arr)
    for i in range(n):
        # Flag to track if any swaps occurred in this pass
        swapped = False
        
        # Reduce the number of comparisons in each pass
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr