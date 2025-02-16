def flatten_nested_list(nested_list):
    """
    Flatten a nested list of arbitrary depth into a single-level list.
    
    Args:
        nested_list (list): A potentially nested list to be flattened.
    
    Returns:
        list: A flattened list containing all elements from the input list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
    
    flattened = []
    
    def _recursive_flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                _recursive_flatten(sub_item)
        else:
            flattened.append(item)
    
    _recursive_flatten(nested_list)
    return flattened