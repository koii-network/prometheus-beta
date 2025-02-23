def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    Args:
        arr (list): A sorted list of comparable elements (ascending order)
        target: The element to search for in the array
    
    Returns:
        int: Index of the target element if found, -1 otherwise
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is not sorted
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Edge case: empty list
    if not arr:
        return -1
    
    # Binary search implementation
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Calculate mid to prevent integer overflow
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