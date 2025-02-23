from typing import List, Any

def flatten_nested_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a nested list of arbitrary depth into a single-level list.

    This function recursively unpacks nested lists, preserving the order 
    of elements and handling various types of nested structures.

    Args:
        nested_list (List[Any]): A potentially nested list to be flattened.

    Returns:
        List[Any]: A flattened list containing all non-list elements.

    Examples:
        >>> flatten_nested_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_nested_list([])
        []
        >>> flatten_nested_list([1, 2, 3])
        [1, 2, 3]
    """
    # Handle non-list and empty list cases
    if not isinstance(nested_list, list):
        return [nested_list]
    
    if not nested_list:
        return []
    
    # Recursive flattening
    flattened = []
    for item in nested_list:
        # Recursively handle nested lists
        if isinstance(item, list):
            flattened.extend(flatten_nested_list(item))
        else:
            flattened.append(item)
    
    return flattened