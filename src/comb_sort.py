def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list.
    
    Comb Sort is an improvement over Bubble Sort. The basic idea is to eliminate 
    turtles, or small values near the end of the list, since in a bubble sort these 
    slow the sorting down tremendously.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Define the initial gap (shrink factor of 1.3 is typical)
    gap = len(arr)
    shrink = 1.3
    
    # Flag to track if any swaps occurred
    swapped = True
    
    while gap > 1 or swapped:
        # Update gap size
        gap = max(1, int(gap / shrink))
        
        # Reset swap flag
        swapped = False
        
        # Compare elements with current gap
        for i in range(len(arr) - gap):
            try:
                if arr[i] > arr[i + gap]:
                    # Swap elements
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
            except TypeError:
                raise ValueError("List contains elements that cannot be compared")
    
    return arr