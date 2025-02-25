def find_list_difference(list1, list2):
    """
    Find the difference between two lists.
    
    Args:
        list1 (list): The first list
        list2 (list): The second list
    
    Returns:
        dict: A dictionary containing:
            - 'added': Elements in list2 that are not in list1
            - 'removed': Elements in list1 that are not in list2
    """
    # Convert lists to sets for efficient comparison
    set1 = set(list1)
    set2 = set(list2)
    
    # Find elements added (in list2 but not in list1)
    added = list(set2 - set1)
    
    # Find elements removed (in list1 but not in list2)
    removed = list(set1 - set2)
    
    return {
        'added': added,
        'removed': removed
    }