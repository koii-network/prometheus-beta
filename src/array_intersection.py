def find_array_intersection(arr1, arr2):
    """
    Find the intersection of two input arrays of integers.

    Args:
        arr1 (list): First input array of integers
        arr2 (list): Second input array of integers

    Returns:
        list: A sorted list of unique integers that are common to both input arrays

    Raises:
        TypeError: If input is not a list or contains non-integer elements
    """
    # Validate input types
    if not (isinstance(arr1, list) and isinstance(arr2, list)):
        raise TypeError("Inputs must be lists")
    
    # Validate that all elements are integers
    if not (all(isinstance(x, int) for x in arr1) and 
            all(isinstance(x, int) for x in arr2)):
        raise TypeError("All array elements must be integers")
    
    # Convert to sets for efficient intersection, then back to sorted list
    return sorted(list(set(arr1) & set(arr2)))