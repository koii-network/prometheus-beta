def flatten_nested_list(nested_list):
    """
    Flatten a nested list of arbitrary depth into a single-level list.
    
    Args:
        nested_list (list): A potentially nested list to be flattened.
    
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