def find_first_index(numbers: list[int], target: int) -> int:
    """
    Find the index of the first occurrence of a target value in a list of integers.

    Args:
        numbers (list[int]): A list of integers to search through
        target (int): The value to find in the list

    Returns:
        int: The index of the first occurrence of the target value,
             or -1 if the target is not found in the list

    Examples:
        >>> find_first_index([1, 2, 3, 4, 3], 3)
        2
        >>> find_first_index([1, 2, 3, 4, 5], 6)
        -1
        >>> find_first_index([], 1)
        -1
    """
    # Handle empty list case first
    if not numbers:
        return -1
    
    # Iterate through the list to find the first occurrence
    for index, value in enumerate(numbers):
        if value == target:
            return index
    
    # If target is not found, return -1
    return -1