def find_intersection(list1, list2):
    """
    Find the intersection of two lists.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing common elements between list1 and list2
    """
    # Convert lists to sets for efficient intersection
    set1 = set(list1)
    set2 = set(list2)
    
    # Return the intersection as a list
    return list(set1.intersection(set2))