def selection_sort(arr):
    """
    Implement the selection sort algorithm to sort a list in-place.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr
    
    # Perform selection sort
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, len(arr)):
            # Compare elements to find the minimum
            try:
                if arr[j] < arr[min_idx]:
                    min_idx = j
            except TypeError:
                raise TypeError("List contains elements that cannot be compared")
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr