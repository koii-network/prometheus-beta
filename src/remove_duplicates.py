from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(arr: List[T]) -> List[T]:
    """
    Remove duplicate elements from an array while maintaining O(n) time complexity.
    
    Args:
        arr (List[T]): Input list with potential duplicates
    
    Returns:
        List[T]: A new list with duplicates removed, preserving original order
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 1, 5])
        [1, 2, 3, 5]
        >>> remove_duplicates(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']
    """
    # Handle edge cases
    if not arr:
        return []
    
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in arr:
        # Only add to result if not seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result