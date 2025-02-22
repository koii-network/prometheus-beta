def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target element.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
    
    Returns:
        int: Index of the target element if found, -1 otherwise
    """
    # Check for empty array
    if not arr:
        return -1
    
    # Initialize left and right pointers
    left, right = 0, len(arr) - 1
    
    # Perform binary search
    while left <= right:
        # Calculate middle index to avoid potential integer overflow
        mid = left + (right - left) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found
    return -1