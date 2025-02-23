def is_sorted(lst, ascending=True):
    """
    Check if a list is sorted in ascending or descending order.

    Args:
        lst (list): The input list to check for sorting.
        ascending (bool, optional): 
            - If True, check for ascending order (default). 
            - If False, check for descending order.

    Returns:
        bool: True if the list is sorted according to the specified order, 
              False otherwise.

    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.

    Examples:
        >>> is_sorted([1, 2, 3, 4])
        True
        >>> is_sorted([4, 3, 2, 1], ascending=False)
        True
        >>> is_sorted([])
        True
        >>> is_sorted([1])
        True
    """
    # Handle empty or single-element lists
    if len(lst) <= 1:
        return True

    # Determine comparison function based on ascending parameter
    if ascending:
        compare = lambda x, y: x <= y
    else:
        compare = lambda x, y: x >= y

    # Check each pair of adjacent elements
    for i in range(len(lst) - 1):
        if not compare(lst[i], lst[i+1]):
            return False

    return True