def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        arr1 (list): First sorted input array 
        arr2 (list): Second sorted input array
    
    Returns:
        list: A new sorted array containing all elements from both input arrays
    
    Raises:
        TypeError: If input arrays are not lists
        ValueError: If input arrays are not sorted
    """
    # Validate input types
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Inputs must be lists")
    
    # Check if arrays are sorted
    if arr1 != sorted(arr1) or arr2 != sorted(arr2):
        raise ValueError("Input arrays must be sorted")
    
    # Merge arrays efficiently
    merged = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Add remaining elements from either array
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged