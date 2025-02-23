def find_list_intersection(list1, list2):
    """
    Find the intersection of two lists, returning a list of common elements.

    Args:
        list1 (list): The first input list
        list2 (list): The second input list

    Returns:
        list: A list containing unique elements common to both input lists,
              preserving the order of first occurrence in list1

    Notes:
        - Returns an empty list if no common elements are found
        - Preserves the order of first occurrence in list1
        - Handles lists of different types
        - Handles duplicate elements correctly
    """
    # Use a set for efficient lookup and to track unique common elements
    common_elements = []
    seen = set()
    
    for item in list1:
        # Check if the item is in list2 and hasn't been added before
        if item in set(list2) and item not in seen:
            common_elements.append(item)
            seen.add(item)
    
    return common_elements