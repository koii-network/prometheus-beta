def linear_search(arr, target):
    """
    Perform a linear search to find the index of a target element in a list.
    
    Args:
        arr (list): The list to search through
        target: The element to search for
    
    Returns:
        int: The index of the target element if found, -1 otherwise
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1