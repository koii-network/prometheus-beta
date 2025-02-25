def remove_duplicates(arr):
    """
    Remove duplicate elements from an array while maintaining O(n) time complexity.
    
    This function uses a set to achieve linear time complexity for duplicate removal.
    
    Args:
        arr (list): Input list that may contain duplicate elements
    
    Returns:
        list: A new list with duplicates removed, preserving the order of first occurrence
    
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
    # Handle empty list case
    if not arr:
        return []
    
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in arr:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result