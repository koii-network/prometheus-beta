def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list of comparable elements.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Create a copy of the input list to avoid modifying the original
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a mutable copy of the list
    lst = arr.copy()
    
    # Initial gap (shrink factor of 1.3 is standard for Comb Sort)
    gap = len(lst)
    shrink = 1.3
    
    # Flag to track if any swaps occurred
    swapped = True
    
    while gap > 1 or swapped:
        # Update gap
        gap = max(1, int(gap / shrink))
        
        # Reset swap flag
        swapped = False
        
        # Compare elements with current gap
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                # Swap elements
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    
    return lst