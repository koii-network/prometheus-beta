def is_list_sorted(lst, ascending=True):
    """
    Check if a list is sorted in ascending or descending order.
    
    Args:
        lst (list): The list to check for sorting.
        ascending (bool, optional): Determines sorting direction. 
            True for ascending, False for descending. Defaults to True.
    
    Returns:
        bool: True if the list is sorted, False otherwise.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    # Empty or single-element lists are considered sorted
    if len(lst) <= 1:
        return True
    
    # Check sorting direction
    if ascending:
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    else:
        return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))