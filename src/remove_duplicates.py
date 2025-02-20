def remove_duplicates(input_list):
    """
    Remove duplicate values from a list while maintaining the original order.
    
    Args:
        input_list (list): A list of integers with potential duplicates.
    
    Returns:
        list: A new list with duplicates removed, preserving the original order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Type checking
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Use dict.fromkeys to maintain order and remove duplicates 
    # This is an efficient O(n) space and time complexity solution
    return list(dict.fromkeys(input_list))