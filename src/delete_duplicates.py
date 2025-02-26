def deleteDuplicates(arr):
    """
    Remove duplicate elements from the input array while preserving the original order.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed, maintaining the original order of first occurrence
    
    Raises:
        TypeError: If input is not a list
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in arr:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result