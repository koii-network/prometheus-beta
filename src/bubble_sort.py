def bubble_sort(arr):
    """
    Implement the bubble sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Get the length of the list
    n = len(sorted_arr)
    
    # Outer loop for passes
    for i in range(n):
        # Flag to optimize by detecting if any swaps occurred
        swapped = False
        
        # Inner loop for comparisons and swapping
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            try:
                if sorted_arr[j] > sorted_arr[j + 1]:
                    # Swap elements if they are in the wrong order
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    swapped = True
            except TypeError:
                raise TypeError("List contains elements that cannot be compared")
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return sorted_arr