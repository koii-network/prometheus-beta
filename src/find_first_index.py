def find_first_index(numbers: list[int], target: int) -> int:
    """
    Find the index of the first occurrence of a target value in a list of integers.

    Args:
        numbers (list[int]): A list of integers to search through
        target (int): The value to find in the list

    Returns:
        int: The index of the first occurrence of the target value,
             or -1 if the target is not found in the list

    Raises:
        TypeError: If numbers is not a list or target is not an integer

    Examples:
        >>> find_first_index([1, 2, 3, 4, 3], 3)
        2
        >>> find_first_index([1, 2, 3, 4, 5], 6)
        -1
        >>> find_first_index([], 1)
        -1
    """
    # Type checking
    if not isinstance(numbers, list):
        raise TypeError("First argument must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Handle empty list case first
    if not numbers:
        return -1
    
    # Ensure all elements in the list are integers
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements in the list must be integers")
    
    # Iterate through the list to find the first occurrence
    for index, value in enumerate(numbers):
        if value == target:
            return index
    
    # If target is not found, return -1
    return -1