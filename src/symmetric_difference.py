def symmetric_difference(list1, list2):
    """
    Find the symmetric difference between two lists.
    
    The symmetric difference is a set of elements which are in either of the lists,
    but not in their intersection.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing elements that are in either list1 or list2, but not both
    """
    # Convert lists to sets to remove duplicates and enable set operations
    set1 = set(list1)
    set2 = set(list2)
    
    # Use symmetric_difference method to find elements unique to both sets
    symmetric_diff_set = set1.symmetric_difference(set2)
    
    # Convert back to a list and return
    return list(symmetric_diff_set)