def count_matching_elements(arr1, arr2):
    """
    Count the number of elements in arr1 that are also present in arr2.
    
    Args:
        arr1 (list): First list of integers
        arr2 (list): Second list of integers
    
    Returns:
        int: Number of elements from arr1 that are in arr2
    """
    # Convert arr2 to a set for efficient lookup
    set2 = set(arr2)
    
    # Count elements from arr1 that are in set2
    return sum(1 for elem in arr1 if elem in set2)