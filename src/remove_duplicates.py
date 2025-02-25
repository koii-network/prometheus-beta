def remove_duplicates(arr):
    """
    Remove duplicate elements from the input array while maintaining O(n) time complexity.
    
    Args:
        arr (list): Input list that may contain duplicate elements
    
    Returns:
        list: A new list with duplicates removed, preserving the original order of first occurrence
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([])
        []
        >>> remove_duplicates(['a', 'b', 'a', 'c', 'b'])
        ['a', 'b', 'c']
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