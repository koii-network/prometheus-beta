def remove_duplicates(arr):
    """
    Remove duplicate elements from an array while maintaining O(n) time complexity.
    
    Args:
        arr (list): Input list with potential duplicates
    
    Returns:
        list: A new list with duplicates removed, preserving the original order of first occurrence
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Use a set to track seen elements and maintain order
    seen = set()
    result = []
    
    for item in arr:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result