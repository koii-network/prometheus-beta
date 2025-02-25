def find_first_index(numbers: list[int], target: int) -> int:
    """
    Find the index of the first occurrence of a target value in a list of integers.

    Args:
        numbers (list[int]): The input list of integers to search
        target (int): The value to find in the list

    Returns:
        int: The index of the first occurrence of the target value,
             or -1 if the target is not found in the list

    Examples:
        >>> find_first_index([1, 2, 3, 4, 3], 3)
        2
        >>> find_first_index([1, 2, 3, 4], 5)
        -1
        >>> find_first_index([], 1)
        -1
    """
    try:
        # Use a single pass through the list with built-in index method
        return numbers.index(target) if target in numbers else -1
    except (TypeError, ValueError):
        # Handle cases with invalid input types or non-indexable objects
        return -1