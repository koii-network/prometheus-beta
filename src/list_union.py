def find_list_union(list1, list2):
    """
    Find the union of two lists, removing duplicates and maintaining order.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing unique elements from both input lists, 
              preserving the order of first occurrence
    """
    # Use a dictionary to preserve order and remove duplicates
    union_dict = {}
    for item in list1 + list2:
        union_dict[item] = None
    
    return list(union_dict.keys())