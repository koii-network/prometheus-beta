def deleteDuplicates(arr):
    """
    Removes duplicate elements from the input array while maintaining the original order.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: Modified list with duplicates removed, preserving original order
    """
    # Use a set to track seen elements while maintaining order
    seen = set()
    result = []
    
    for item in arr:
        # Only add the item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result