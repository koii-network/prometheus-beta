def remove_duplicates(arr):
    """
    Remove duplicate values from an array, preserving the order of first occurrence.
    
    Args:
        arr (list): Input list with potential duplicate values
    
    Returns:
        list: A new list with duplicates removed, maintaining original order
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use dict.fromkeys to preserve order and remove duplicates
    return list(dict.fromkeys(arr))