def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list in ascending order.
    
    Comb Sort is an improvement over Bubble Sort. The idea is to eliminate turtles,
    or small values near the end of the list, since in Bubble Sort these slow down 
    the sorting process.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        TypeError: If the list contains elements that cannot be compared
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Initialize the gap
    gap = len(arr)
    
    # Define shrink factor (typically around 1.3)
    shrink = 1.3
    
    # Flag to track if any swaps occurred
    swapped = True
    
    while gap > 1 or swapped:
        # Update gap
        gap = max(1, int(gap / shrink))
        
        # Reset swap flag
        swapped = False
        
        # Compare and swap elements with current gap
        for i in range(len(arr) - gap):
            try:
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
            except TypeError:
                raise TypeError("List contains elements that cannot be compared")
    
    return arr