def remove_duplicates(arr):
    """
    Remove duplicate elements from an array while maintaining O(n) time complexity.
    
    Args:
        arr (list): Input list that may contain duplicate elements
    
    Returns:
        list: A new list with duplicates removed, preserving the order of first occurrence
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([])
        []
    """
    # Handle edge cases
    if not arr:
        return []
    
    # Use a set to track unique elements and preserve order
    seen = set()
    result = []
    
    for item in arr:
        # Only add the item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result