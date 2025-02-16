def find_list_union(list1, list2):
    """
    Find the union of two lists, removing duplicates while preserving order.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing unique elements from both input lists in order of first appearance
    """
    # Use a dict to preserve order and remove duplicates (Python 3.7+)
    union_dict = dict.fromkeys(list1 + list2)
    return list(union_dict)