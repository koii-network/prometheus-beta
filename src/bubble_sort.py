def bubble_sort(arr):
    """
    Perform bubble sort with an optimization to avoid unnecessary swapping.
    
    This implementation uses a 'swapped' flag to detect if the list is already 
    sorted and can terminate early if no swaps are made in a pass.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, it's already sorted
    n = len(arr)
    if n <= 1:
        return arr
    
    # Outer loop for passes
    for i in range(n):
        # Optimization: Assume list is sorted until a swap happens
        swapped = False
        
        # Inner loop for comparisons and swapping
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Mark that a swap occurred
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return arr