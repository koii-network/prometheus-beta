def symmetric_difference(list1, list2):
    """
    Find the symmetric difference between two lists.
    
    The symmetric difference is a set of elements which are in either of the lists,
    but not in their intersection.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list of elements that are in either list1 or list2, but not both
    """
    # Convert lists to sets to use set operations
    set1 = set(list1)
    set2 = set(list2)
    
    # Compute symmetric difference and convert back to list
    symmetric_diff = list(set1.symmetric_difference(set2))
    
    return symmetric_diff