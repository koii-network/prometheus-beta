def find_common(list1, list2):
    """
    Find and return a list of elements common to both input lists.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list of elements that appear in both input lists
    """
    # Convert lists to sets for efficient intersection
    set1 = set(list1)
    set2 = set(list2)
    
    # Return the list of common elements
    return list(set1.intersection(set2))