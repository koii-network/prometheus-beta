def list_union(list1, list2):
    """
    Find the union of two lists, removing duplicates.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing unique elements from both input lists
    """
    return list(set(list1 + list2))