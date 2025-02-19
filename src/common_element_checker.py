def has_common_element(arr1, arr2):
    """
    Check if two arrays have at least one common element.
    
    Time complexity: O(n)
    Space complexity: O(n)
    
    Args:
        arr1 (list): First input array
        arr2 (list): Second input array
    
    Returns:
        bool: True if arrays have a common element, False otherwise
    """
    # Create a set from the first array for O(1) lookup
    set1 = set(arr1)
    
    # Check for common elements in O(n) time
    for item in arr2:
        if item in set1:
            return True
    
    return False