def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list.
    
    Comb Sort is an improvement over Bubble Sort that uses a gap sequence to 
    compare and swap elements, reducing the number of swaps needed.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Initialize gap and shrink factor
    gap = len(arr)
    shrink = 1.3  # Recommended shrink factor
    
    # Flag to track if any swaps occurred
    swapped = True
    
    while gap > 1 or swapped:
        # Calculate next gap
        gap = max(1, int(gap / shrink))
        
        # Reset swap flag
        swapped = False
        
        # Compare elements with current gap
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                # Swap elements
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    
    return arr