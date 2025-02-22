def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        arr1 (list): First sorted input array 
        arr2 (list): Second sorted input array
    
    Returns:
        list: A new sorted array containing all elements from arr1 and arr2
    """
    merged = []
    i, j = 0, 0
    
    # Compare and merge elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1, if any
    merged.extend(arr1[i:])
    
    # Add remaining elements from arr2, if any
    merged.extend(arr2[j:])
    
    return merged