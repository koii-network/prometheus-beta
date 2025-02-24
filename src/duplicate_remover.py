def deleteDuplicates(arr):
    """
    Remove duplicate elements from the input array while preserving the original order.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed, maintaining the original order of first occurrences
    
    Examples:
        >>> deleteDuplicates([1, 2, 3, 2, 1, 5, 6, 5])
        [1, 2, 3, 5, 6]
        >>> deleteDuplicates([])
        []
        >>> deleteDuplicates([1, 1, 1, 1])
        [1]
    """
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in arr:
        # Only add the item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result