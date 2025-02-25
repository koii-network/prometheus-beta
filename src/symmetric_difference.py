def find_symmetric_difference(list1, list2):
    """
    Find the symmetric difference between two lists.
    
    The symmetric difference is a set of elements which are in either of the lists,
    but not in their intersection.
    
    Args:
        list1 (list): The first input list
        list2 (list): The second input list
    
    Returns:
        list: A list containing elements that are in either list1 or list2, but not both
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Inputs must be lists")
    
    # Convert lists to sets for efficient symmetric difference calculation
    set1 = set(list1)
    set2 = set(list2)
    
    # Calculate symmetric difference and convert back to a list
    return list(set1.symmetric_difference(set2))