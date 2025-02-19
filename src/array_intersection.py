def find_array_intersection(arr1, arr2):
    """
    Find the intersection of two integer arrays.
    
    Args:
        arr1 (list): First input array of integers
        arr2 (list): Second input array of integers
    
    Returns:
        list: A new array containing common elements between arr1 and arr2
    """
    # Convert arrays to sets for efficient intersection
    # Use set intersection to find common elements
    # Convert back to a sorted list to ensure consistent output
    return sorted(list(set(arr1) & set(arr2)))