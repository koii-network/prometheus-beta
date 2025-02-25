def find_list_union(list1, list2):
    """
    Find the union of two lists, removing duplicates and preserving order.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        list: A list containing unique elements from both input lists, 
              preserving the order of first occurrence.

    Raises:
        TypeError: If input arguments are not lists.
    """
    # Validate input types
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both arguments must be lists")
    
    # Use dict.fromkeys to preserve order and remove duplicates
    return list(dict.fromkeys(list1 + list2))