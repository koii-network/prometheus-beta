def has_common_element(arr1, arr2):
    """
    Check if two arrays have at least one common element.
    
    Time Complexity: O(n), where n is the total number of elements in both arrays
    Space Complexity: O(n) to store unique elements from one array
    
    Args:
        arr1 (list): First input array
        arr2 (list): Second input array
    
    Returns:
        bool: True if arrays have at least one common element, False otherwise
    
    Raises:
        TypeError: If inputs are not lists or lists containing comparable elements
    """
    # Validate input types
    if not (isinstance(arr1, list) and isinstance(arr2, list)):
        raise TypeError("Inputs must be lists")
    
    # If either array is empty, there can be no common elements
    if not arr1 or not arr2:
        return False
    
    # Create a set from the first array for O(1) lookup
    unique_elements = set(arr1)
    
    # Check if any element from the second array exists in the set
    for item in arr2:
        if item in unique_elements:
            return True
    
    return False