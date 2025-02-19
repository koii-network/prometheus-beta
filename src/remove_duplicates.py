def remove_duplicates(arr):
    """
    Remove duplicate elements from an array while maintaining O(n) time complexity.
    
    Args:
        arr (list): Input list that may contain duplicates
    
    Returns:
        list: A new list with duplicates removed, preserving the original order
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Use a set to track seen elements for O(1) lookup
    seen = set()
    # Use a list to preserve order
    unique_list = []
    
    for item in arr:
        # Only add to unique_list if not seen before
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    
    return unique_list