def flatten_nested_list(nested_list):
    """
    Flatten a potentially deeply nested list into a single-level list.
    
    Args:
        nested_list (list): A list that may contain nested lists at any depth.
    
    Returns:
        list: A flattened version of the input list.
    
    Raises:
        TypeError: If the input is not a list.
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