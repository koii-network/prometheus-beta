def find_first_index(arr, target):
    """
    Find the index of the first occurrence of a target value in an array.

    Args:
        arr (list): The input array to search through
        target: The value to search for in the array

    Returns:
        int: The index of the first occurrence of the target value,
             or -1 if the target is not found

    Examples:
        >>> find_first_index([1, 2, 3, 4, 3], 3)
        2
        >>> find_first_index([1, 2, 3, 4], 5)
        -1
        >>> find_first_index([], 1)
        -1
    """
    # Handle empty array case
    if not arr:
        return -1
    
    # Iterate through the array and return the index of first match
    for index, value in enumerate(arr):
        if value == target:
            return index
    
    # Return -1 if no match is found
    return -1