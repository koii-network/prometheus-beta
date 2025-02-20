def bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations
    by tracking whether any swaps occurred in each pass.
    
    Args:
        arr (list): List of comparable elements to be sorted
    
    Returns:
        list: Sorted list in ascending order
    """
    n = len(arr)
    
    # Optimization: Track if any swaps occurred
    for i in range(n):
        # Flag to detect if any swaps happened in this pass
        swapped = False
        
        # Reduce number of comparisons in each subsequent pass
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr