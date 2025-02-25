def has_common_element(arr1, arr2):
    """
    Check if two arrays have at least one common element.
    
    Args:
        arr1 (list): First input array
        arr2 (list): Second input array
    
    Returns:
        bool: True if arrays have at least one common element, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If inputs are not lists
    """
    # Validate input types
    if not (isinstance(arr1, list) and isinstance(arr2, list)):
        raise TypeError("Inputs must be lists")
    
    # Use a set for O(n) lookup time
    unique_elements = set(arr1)
    
    # Check for common elements in O(n) time
    for element in arr2:
        if element in unique_elements:
            return True
    
    return False