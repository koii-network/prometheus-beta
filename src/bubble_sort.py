def bubble_sort(arr):
    """
    Implement the bubble sort algorithm to sort a list of comparable elements.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Get the length of the list
    n = len(sorted_arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize the algorithm by breaking early if no swaps occur
        swapped = False
        
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return sorted_arr