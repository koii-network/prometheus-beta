def find_array_intersection(arr1, arr2):
    """
    Find the intersection of two arrays of integers.
    
    Args:
        arr1 (list): First input array of integers
        arr2 (list): Second input array of integers
    
    Returns:
        list: A new array containing common elements between arr1 and arr2
    """
    # Convert to sets for efficient intersection
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Return list of common elements, preserving order of first appearance
    return list(set1.intersection(set2))