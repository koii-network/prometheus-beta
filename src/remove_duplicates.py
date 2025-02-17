def remove_duplicates(arr):
    """
    Remove duplicate values from an array while preserving the original order.
    
    Args:
        arr (list): Input list that may contain duplicate values.
    
    Returns:
        list: A new list with duplicates removed, keeping the first occurrence of each value.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen values while preserving order
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result