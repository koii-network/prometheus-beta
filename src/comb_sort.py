def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list in ascending order.
    
    Comb sort is an improvement over bubble sort. It eliminates turtles (small values 
    near the end of the list) by using a gap that decreases in each iteration.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Define initial gap using Shrink factor of 1.3
    gap = len(arr)
    shrink = 1.3
    
    while gap > 1:
        # Update gap
        gap = max(int(gap / shrink), 1)
        
        # Track whether any swaps occur
        swapped = False
        
        # Compare elements with current gap
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                # Swap elements
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
        
        # If no swaps occurred and gap is 1, list is sorted
        if not swapped and gap == 1:
            break
    
    return arr