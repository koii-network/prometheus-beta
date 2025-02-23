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
        - Preserves the order of first occurrence of elements
        - Handles lists of any hashable type
        - Removes duplicates in the resulting intersection
    """
    # Convert lists to sets for efficient intersection, then convert back to list
    # Use dict.fromkeys to preserve order of first occurrence while removing duplicates
    return list(dict.fromkeys(elem for elem in list1 if elem in list2))