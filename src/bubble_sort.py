def optimized_bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    Key optimizations:
    1. Track if any swaps occurred in each pass
    2. Reduce iterations for already sorted portions of the list
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list
    """
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        # Flag to track if any swaps occurred in this pass
        swapped = False
        
        # Reduce the range of iterations in each pass
        # The last i elements are already in their correct positions
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