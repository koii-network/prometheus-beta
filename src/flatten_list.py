def flatten_nested_list(nested_list):
    """
    Flatten a potentially nested list into a single-level list.
    
    Args:
        nested_list (list): A list that may contain nested lists
    
    Returns:
        list: A flattened list with all elements at a single level
    
    Raises:
        TypeError: If the input is not a list
    """
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
    
    flattened = []
    
    def recursive_flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                recursive_flatten(sub_item)
        else:
            flattened.append(item)
    
    recursive_flatten(nested_list)
    return flattened