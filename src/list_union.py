def list_union(list1, list2):
    """
    Find the union of two lists, removing duplicates and preserving order.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing unique elements from both input lists, 
              preserving the order of first occurrence
    """
    # Use a list to maintain order and remove duplicates
    union_list = []
    
    # Add elements from list1, avoiding duplicates
    for item in list1:
        if item not in union_list:
            union_list.append(item)
    
    # Add elements from list2, avoiding duplicates
    for item in list2:
        if item not in union_list:
            union_list.append(item)
    
    return union_list