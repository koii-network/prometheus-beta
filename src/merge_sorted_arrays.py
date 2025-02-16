def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        arr1 (list): First sorted input array 
        arr2 (list): Second sorted input array
    
    Returns:
        list: A new sorted array containing all elements from arr1 and arr2
    
    Raises:
        TypeError: If inputs are not lists
        ValueError: If input lists are not sorted
    """
    # Type checking
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Inputs must be lists")
    
    # Verify input arrays are sorted
    if not all(arr1[i] <= arr1[i+1] for i in range(len(arr1)-1)) or \
       not all(arr2[i] <= arr2[i+1] for i in range(len(arr2)-1)):
        raise ValueError("Input arrays must be sorted in ascending order")
    
    # Merge the two sorted arrays
    merged = []
    i, j = 0, 0
    
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