def is_sorted(lst):
    """
    Check if a list is sorted in ascending order.
    
    Args:
        lst (list): The list to check for sorting.
    
    Returns:
        bool: True if the list is sorted in ascending order, False otherwise.
    
    Raises:
        TypeError: If the input is not a list or contains elements that cannot be compared.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    # Empty or single-element lists are considered sorted
    if len(lst) <= 1:
        return True
    
    # Compare each element with the next to check if sorted
    try:
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    except TypeError:
        raise TypeError("List contains elements that cannot be compared")