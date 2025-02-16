def symmetric_difference(list1, list2):
    """
    Find the symmetric difference between two lists.
    
    The symmetric difference contains elements that are in either list,
    but not in both (elements unique to each list).
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing elements unique to list1 and list2
    """
    # Convert lists to sets to use built-in symmetric difference operation
    set1 = set(list1)
    set2 = set(list2)
    
    # Return symmetric difference as a list
    return list(set1.symmetric_difference(set2))