def find_list_intersection(list1, list2):
    """
    Find the intersection of two lists.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing common elements between list1 and list2
    """
    # Convert lists to sets to use built-in intersection method
    # This ensures unique elements and efficient intersection
    return list(set(list1) & set(list2))