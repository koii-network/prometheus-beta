def remove_duplicates(arr):
    """
    Remove duplicate values from an array while preserving the original order.
    
    Args:
        arr (list): Input list that may contain duplicate values
    
    Returns:
        list: A new list with duplicates removed, maintaining the order of first occurrence
    """
    # Use a set to track seen values while maintaining order
    seen = set()
    result = []
    
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result