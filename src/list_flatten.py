from typing import List, Union

def flatten_list(nested_list: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested list of integers to a single-level list.

    This function recursively flattens a nested list, handling lists 
    nested to any depth. Only integer elements are preserved.

    Args:
        nested_list (List[Union[int, List]]): A potentially nested list of integers

    Returns:
        List[int]: A flattened list of integers

    Raises:
        TypeError: If non-integer non-list elements are encountered
    """
    flattened = []
    
    for item in nested_list:
        if isinstance(item, int):
            flattened.append(item)
        elif isinstance(item, list):
            # Recursively flatten nested lists
            flattened.extend(flatten_list(item))
        else:
            raise TypeError(f"Unsupported type in list: {type(item)}")
    
    return flattened