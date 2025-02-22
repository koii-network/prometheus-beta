def flatten_nested_list(nested_list):
    """
    Flatten a nested list of arbitrary depth into a single-level list.
    
    Args:
        nested_list (list): A list that may contain nested lists
    
    Returns:
        list: A flattened version of the input list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check if input is a list
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
    
    # Initialize result list
    flattened = []
    
    # Recursive helper function to flatten
    def _flatten(item):
        # If item is a list, recursively flatten it
        if isinstance(item, list):
            for sub_item in item:
                _flatten(sub_item)
        else:
            # If item is not a list, append to flattened result
            flattened.append(item)
    
    # Start the flattening process
    _flatten(nested_list)
    
    return flattened