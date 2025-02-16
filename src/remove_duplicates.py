def remove_duplicates(arr):
    """
    Remove duplicate values from an input array while preserving the original order.
    
    Args:
        arr (list): Input list that may contain duplicate values
    
    Returns:
        list: A new list with duplicates removed, maintaining the order of first occurrence
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result