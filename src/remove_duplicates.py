def remove_duplicates(input_list):
    """
    Remove duplicate values from a list while maintaining the original order.
    
    Args:
        input_list (list): A list of integers with potential duplicates.
    
    Returns:
        list: A new list with duplicates removed, preserving the original order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Type checking
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer elements
    if not all(isinstance(x, int) for x in input_list):
        raise ValueError("All elements must be integers")
    
    # Use dictionary to preserve order and remove duplicates
    # dict.fromkeys() maintains first occurrence order in Python 3.7+
    return list(dict.fromkeys(input_list))