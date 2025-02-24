def remove_duplicates(arr):
    """
    Remove duplicate elements from an input array while maintaining the original order.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed, preserving the first occurrence of each element
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([])
        []
        >>> remove_duplicates([1, 1, 1, 1])
        [1]
    """
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in arr:
        # Only add to result if not seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result