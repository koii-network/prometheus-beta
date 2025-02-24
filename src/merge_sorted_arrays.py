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
        ValueError: If input lists are not sorted in ascending order
    """
    # Type checking
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Inputs must be lists")
    
    # Check if arrays are sorted
    if not (is_sorted(arr1) and is_sorted(arr2)):
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

def is_sorted(arr):
    """
    Check if a list is sorted in ascending order.

    Args:
        arr (list): Input list to check

    Returns:
        bool: True if list is sorted, False otherwise
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) if arr else True