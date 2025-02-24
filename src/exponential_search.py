def exponential_search(arr, target):
    """
    Perform exponential search on a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
    
    Returns:
        int: Index of the target element if found, else -1
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the list is empty
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Cannot search in an empty list")
    
    # Handle single element case
    if len(arr) == 1:
        return 0 if arr[0] == target else -1
    
    # Find range for binary search
    if arr[0] == target:
        return 0
    
    # Find the bound to do binary search
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Perform binary search
    left = i // 2
    right = min(i, len(arr) - 1)
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1