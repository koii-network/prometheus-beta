def find_list_intersection(list1, list2):
    """
    Find the intersection of two lists.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing common elements between list1 and list2, 
              with no duplicates and preserving the order of first occurrence
    
    Examples:
        >>> find_list_intersection([1, 2, 3, 4], [3, 4, 5, 6])
        [3, 4]
        >>> find_list_intersection(['a', 'b', 'c'], ['b', 'c', 'd'])
        ['b', 'c']
        >>> find_list_intersection([], [1, 2, 3])
        []
    """
    # Convert lists to sets for efficient intersection, then convert back to list 
    # while preserving order of first occurrence
    intersection = list(dict.fromkeys(x for x in list1 if x in list2))
    return intersection