def binary_search(arr, target):
    """
    Implement binary search algorithm to find the index of a target in a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
    
    Returns:
        int: Index of the target if found, otherwise -1
    """
    # Validate input
    if not arr:
        return -1
    
    # Initialize left and right pointers
    left = 0
    right = len(arr) - 1
    
    # Perform binary search
    while left <= right:
        # Calculate middle index
        mid = (left + right) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        if arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found
    return -1