def linear_search(arr, target):
    """
    Perform a linear search on the given array to find the target element.
    
    Args:
        arr (list): The list to search through
        target: The element to search for
    
    Returns:
        int: The index of the target element if found, -1 otherwise
    """
    # Iterate through each element in the array
    for index, element in enumerate(arr):
        # If the current element matches the target, return its index
        if element == target:
            return index
    
    # If the target is not found, return -1
    return -1