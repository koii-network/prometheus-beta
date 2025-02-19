def find_common(list1, list2):
    """
    Find common elements between two input lists.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list of elements common to both input lists
    """
    # Convert lists to sets for efficient comparison
    set1 = set(list1)
    set2 = set(list2)
    
    # Return the intersection of the two sets as a list
    return list(set1.intersection(set2))