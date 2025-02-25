def find_list_difference(list1, list2):
    """
    Find the difference between two lists.

    This function returns a dictionary containing:
    - 'added': elements in list2 that are not in list1
    - 'removed': elements in list1 that are not in list2
    - 'unchanged': elements that are common to both lists

    Args:
        list1 (list): The first input list
        list2 (list): The second input list

    Returns:
        dict: A dictionary with 'added', 'removed', and 'unchanged' lists

    Raises:
        TypeError: If the input arguments are not lists
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists")

    # Convert to sets for efficient comparison
    set1 = set(list1)
    set2 = set(list2)

    # Calculate differences
    added = list(set2 - set1)
    removed = list(set1 - set2)
    unchanged = list(set1 & set2)

    return {
        'added': sorted(added),
        'removed': sorted(removed),
        'unchanged': sorted(unchanged)
    }