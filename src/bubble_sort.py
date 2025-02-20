def optimized_bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    The optimization includes:
    1. A flag to track if any swaps occurred in an iteration
    2. Reducing the number of comparisons in subsequent passes
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list
    """
    n = len(arr)
    
    # Outer loop - passes through the list
    for i in range(n):
        # Flag to optimize - track if any swapping occurred
        swapped = False
        
        # Inner loop - compare and swap adjacent elements
        # Reduce the range of comparison in each pass
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return arr