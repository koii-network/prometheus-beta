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
    # Check if input is a list
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
    
    # Initialize the flattened list
    flattened = []
    
    # Recursive helper function to flatten the list
    def _flatten(item):
        # If the item is a list, recursively flatten its contents
        if isinstance(item, list):
            for sub_item in item:
                _flatten(sub_item)
        else:
            # If the item is not a list, append it to the flattened list
            flattened.append(item)
    
    # Start the flattening process
    _flatten(nested_list)
    
    return flattened