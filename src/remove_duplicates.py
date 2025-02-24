def remove_duplicates(arr):
    """
    Remove duplicate elements from an array of integers while maintaining 
    the original order of first occurrence.

    Args:
        arr (list): Input list of integers

    Returns:
        list: A new list with duplicates removed, preserving the order 
              of first occurrence

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
    # Handle edge case of empty input
    if not arr:
        return []
    
    # Use a set to track seen elements for O(1) lookup
    seen = set()
    result = []
    
    # Iterate through the array, keeping only first occurrence of each element
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result