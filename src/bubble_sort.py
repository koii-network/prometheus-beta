def optimized_bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    This implementation stops early if no swaps are made in a pass,
    indicating the list is already sorted.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    n = len(arr)
    
    # Outer loop - reduce passes with early stopping
    for i in range(n):
        # Flag to track if any swaps occur in this pass
        swapped = False
        
        # Inner loop for comparing and swapping adjacent elements
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