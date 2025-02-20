def optimized_bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    The optimization includes:
    1. Early stopping when no swaps occur in a pass
    2. Reducing iterations for already sorted portions of the list
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list
    """
    n = len(arr)
    for i in range(n):
        # Flag to track if any swaps occurred in this pass
        swapped = False
        
        # Reduce iterations for already sorted portions
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