def bubble_sort(arr):
    """
    Implement the bubble sort algorithm to sort a list in-place in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list or contains unsortable elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Bubble sort algorithm
    n = len(arr)
    for i in range(n):
        # Flag to optimize by breaking early if no swaps occur
        swapped = False
        
        # Last i elements are already in place, so reduce comparisons
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            try:
                if arr[j] > arr[j + 1]:
                    # Swap elements
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            except TypeError:
                # Handle cases with incomparable types
                raise TypeError("List contains elements that cannot be compared")
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return arr