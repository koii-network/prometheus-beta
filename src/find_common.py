def find_common(list1, list2):
    """
    Find and return a list of elements common to both input lists.

    Args:
        list1 (list): The first input list
        list2 (list): The second input list

    Returns:
        list: A list of elements that appear in both input lists

    Examples:
        >>> find_common([1, 2, 3], [3, 4, 5])
        [3]
        >>> find_common(['a', 'b', 'c'], ['b', 'c', 'd'])
        ['b', 'c']
        >>> find_common([], [1, 2, 3])
        []
    """
    # Convert lists to sets for efficient comparison
    # Use set intersection to find common elements
    # Convert back to list to maintain consistent return type
    return list(set(list1) & set(list2))