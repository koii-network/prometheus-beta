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
    element_set = set(arr1)
    
    # Check if any element from the second array exists in the set
    for element in arr2:
        if element in element_set:
            return True
    
    return False