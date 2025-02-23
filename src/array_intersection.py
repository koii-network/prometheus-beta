def find_array_intersection(arr1, arr2):
    """
    Find the intersection of two arrays of integers.
    
    Args:
        arr1 (list): First input array of integers
        arr2 (list): Second input array of integers
    
    Returns:
        list: A sorted list of unique integers that are common to both input arrays
    """
    # Convert arrays to sets for efficient intersection
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Find the intersection and convert back to a sorted list
    return sorted(list(set1.intersection(set2)))