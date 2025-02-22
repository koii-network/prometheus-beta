def remove_duplicates(arr):
    """
    Remove duplicate elements from an array while maintaining O(n) time complexity.
    
    Args:
        arr (list): Input list of elements
    
    Returns:
        list: A list with duplicates removed, preserving the order of first occurrence
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Use a set for O(1) lookup to track seen elements
    seen = set()
    result = []
    
    for item in arr:
        # Only add item to result if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result