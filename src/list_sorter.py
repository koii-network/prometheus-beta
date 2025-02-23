def is_sorted(lst, ascending=True):
    """
    Check if a list is sorted in ascending or descending order.

    Args:
        lst (list): The list to check for sorting.
        ascending (bool, optional): 
            - If True, check for ascending order (default). 
            - If False, check for descending order.

    Returns:
        bool: True if the list is sorted according to the specified order, False otherwise.

    Raises:
        TypeError: If the input is not a list or contains elements that cannot be compared.

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
    # Handle empty or single-element lists (always considered sorted)
    if len(lst) <= 1:
        return True

    # Validate input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    try:
        # Check sorting based on ascending parameter
        if ascending:
            return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
        else:
            return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    except TypeError:
        # Catch cases where elements cannot be compared
        raise TypeError("List contains elements that cannot be compared")