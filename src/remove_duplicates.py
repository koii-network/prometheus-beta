def remove_duplicates(input_list):
    """
    Remove duplicates from a given list while preserving the original order.

    Args:
        input_list (list): The input list that may contain duplicate elements.

    Returns:
        list: A new list with duplicate elements removed, maintaining the order 
              of first occurrence of each unique element.

    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Use a dictionary to preserve order in Python 3.7+
    # Keys ensure uniqueness, while preserving the first occurrence
    return list(dict.fromkeys(input_list))