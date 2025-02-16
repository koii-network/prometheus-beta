def is_sorted(lst, ascending=True):
    """
    Check if a list is sorted in ascending or descending order.
    
    Args:
        lst (list): The list to check for sorting.
        ascending (bool, optional): If True, check for ascending order. 
                                    If False, check for descending order. 
                                    Defaults to True.
    
    Returns:
        bool: True if the list is sorted, False otherwise.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    # Empty or single-element lists are always considered sorted
    if len(lst) <= 1:
        return True
    
    # Determine comparison function based on ascending parameter
    if ascending:
        # Check if each element is less than or equal to the next
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    else:
        # Check if each element is greater than or equal to the next
        return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))