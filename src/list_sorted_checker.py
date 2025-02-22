def is_list_sorted(lst, reverse=False):
    """
    Check if a list is sorted in ascending or descending order.
    
    Args:
        lst (list): The list to check for sorting.
        reverse (bool, optional): If True, check for descending order. 
                                  If False (default), check for ascending order.
    
    Returns:
        bool: True if the list is sorted, False otherwise.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    # Empty or single-element lists are always considered sorted
    if len(lst) <= 1:
        return True
    
    # Check sorting based on reverse parameter
    if reverse:
        # Check if list is sorted in descending order
        return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    else:
        # Check if list is sorted in ascending order
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))