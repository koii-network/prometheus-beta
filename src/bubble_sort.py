def bubble_sort(arr):
    """
    Perform bubble sort on the input list with an early exit optimization.
    
    This implementation uses a flag to track if any swaps were made during 
    an iteration. If no swaps are made, the list is already sorted, 
    and the algorithm can terminate early.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    n = len(arr)
    if n <= 1:
        return arr
    
    # Outer loop for passes
    for i in range(n):
        # Flag to optimize early exit
        swapped = False
        
        # Inner loop for comparisons and swapping
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set swapped flag
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return arr