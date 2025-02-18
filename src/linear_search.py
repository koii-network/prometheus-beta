def linear_search(arr, target):
    """
    Perform a linear search to find the index of a target element in a list.
    
    Args:
        arr (list): The list to search through
        target: The element to find in the list
    
    Returns:
        int: The index of the target element if found, -1 otherwise
    """
    # Iterate through each element in the list
    for index, element in enumerate(arr):
        # If the current element matches the target, return its index
        if element == target:
            return index
    
    # If the target is not found, return -1
    return -1