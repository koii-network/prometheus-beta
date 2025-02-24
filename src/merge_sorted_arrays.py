def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a single sorted array.

    Args:
        arr1 (list): First sorted input array
        arr2 (list): Second sorted input array

    Returns:
        list: A new sorted array containing all elements from arr1 and arr2

    Raises:
        TypeError: If input is not a list
        ValueError: If input lists are not sorted
    """
    # Type checking
    if not (isinstance(arr1, list) and isinstance(arr2, list)):
        raise TypeError("Inputs must be lists")
    
    # Sorted order checking (assuming non-decreasing order)
    if not (is_sorted(arr1) and is_sorted(arr2)):
        raise ValueError("Input lists must be sorted")
    
    # Merge logic
    merged = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged

def is_sorted(arr):
    """
    Check if a list is sorted in non-decreasing order.

    Args:
        arr (list): Input list to check

    Returns:
        bool: True if list is sorted, False otherwise
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) if arr else True