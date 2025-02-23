def linear_search(arr, target):
    """
    Perform a linear search to find the index of a target element in a list.

    Args:
        arr (list): The list to search through.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, -1 otherwise.

    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Iterate through the list
    for index, element in enumerate(arr):
        # If element matches target, return its index
        if element == target:
            return index
    
    # If target not found, return -1
    return -1