def remove_duplicates(arr):
    """
    Remove duplicate elements from an array of integers while maintaining 
    the original order of first occurrence.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed, preserving original order
    """
    seen = set()
    result = []
    
    for num in arr:
        # Only add to result if not seen before
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result