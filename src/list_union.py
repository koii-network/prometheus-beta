def find_list_union(list1, list2):
    """
    Find the union of two lists, removing duplicates while preserving order.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing unique elements from both input lists, 
              maintaining the order of first occurrence
    """
    # Use dict.fromkeys to preserve order and remove duplicates
    return list(dict.fromkeys(list1 + list2))