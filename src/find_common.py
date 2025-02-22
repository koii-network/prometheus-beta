def find_common(list1, list2):
    """
    Find and return a list of elements common to both input lists.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list of elements that are present in both input lists
    """
    return list(set(list1) & set(list2))