def is_sorted(lst, ascending=True):
    """
    Check if a list is sorted in ascending or descending order.
    
    Args:
        lst (list): The list to check for sorting.
        ascending (bool, optional): Whether to check for ascending order. 
                                    Defaults to True.
    
    Returns:
        bool: True if the list is sorted, False otherwise.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    # Empty or single-element lists are considered sorted
    if len(lst) <= 1:
        return True
    
    # Check ascending order
    if ascending:
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Check descending order
    return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))