def find_list_intersection(list1, list2):
    """
    Find the intersection of two lists, returning a list of common elements.

    Args:
        list1 (list): The first input list
        list2 (list): The second input list

    Returns:
        list: A list containing elements common to both input lists

    Notes:
        - Returns an empty list if no common elements are found
        - Preserves the order of first occurrence in list1
        - Handles lists of different types
        - Handles duplicate elements correctly
    """
    # Use a set for efficient lookup while preserving order
    set2 = set(list2)
    return [item for item in list1 if item in set2]