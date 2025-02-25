def find_first_index(arr, target):
    """
    Find the index of the first occurrence of a target value in an array.

    Args:
        arr (list): The input array to search through.
        target: The value to find in the array.

    Returns:
        int: The index of the first occurrence of the target value,
             or -1 if the target is not found.

    Examples:
        >>> find_first_index([1, 2, 3, 2, 1], 2)
        1
        >>> find_first_index([1, 2, 3], 4)
        -1
        >>> find_first_index([], 1)
        -1
    """
    for i, item in enumerate(arr):
        # Use strict equality to handle edge cases like True/1
        if item is target or item == target:
            return i
    return -1