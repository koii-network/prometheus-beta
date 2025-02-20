def deleteDuplicates(arr):
    """
    Delete all duplicate elements from the array while maintaining the original order.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: Modified list with duplicates removed, preserving the original order
    """
    # Use a set to track seen elements while maintaining order
    seen = set()
    result = []
    
    for num in arr:
        # Only add the element if it hasn't been seen before
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result