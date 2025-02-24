def cocktail_shaker_sort(arr):
    """
    Implement the cocktail shaker sort (bidirectional bubble sort) algorithm.
    
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
    
    # Flag to optimize sorting by detecting if list is already sorted
    swapped = True
    start = 0
    end = len(arr) - 1
    
    while swapped:
        # Reset swapped flag for this pass
        swapped = False
        
        # Forward pass (left to right)
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                # Swap elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        # If no swapping occurred, list is sorted
        if not swapped:
            break
        
        # Reset swapped flag for backward pass
        swapped = False
        
        # Move the end point back by one, as the last element is now in place
        end -= 1
        
        # Backward pass (right to left)
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                # Swap elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        # Move the start point forward
        start += 1
    
    return arr