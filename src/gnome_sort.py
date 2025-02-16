def gnome_sort(arr):
    """
    Implement the Gnome Sort algorithm.
    
    Gnome Sort, also known as Stupid Sort, works by always finding the first 
    pair of adjacent elements where the element is in the wrong order and 
    swapping them, then moving back to the previous elements to continue checking.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # If list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Start at the beginning of the list
    i = 1
    while i < len(arr):
        # If first element or current element is in correct position, move forward
        if i == 0 or arr[i-1] <= arr[i]:
            i += 1
        else:
            # Swap elements and move back to check previous elements
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    
    return arr