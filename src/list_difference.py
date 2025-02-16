def find_list_difference(list1, list2):
    """
    Find the difference between two lists.
    
    Args:
        list1 (list): The first list to compare
        list2 (list): The second list to compare
    
    Returns:
        dict: A dictionary containing:
            - 'only_in_first': Elements unique to list1
            - 'only_in_second': Elements unique to list2
            - 'common': Elements common to both lists
    """
    set1 = set(list1)
    set2 = set(list2)
    
    return {
        'only_in_first': list(set1 - set2),
        'only_in_second': list(set2 - set1),
        'common': list(set1 & set2)
    }