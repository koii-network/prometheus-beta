def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    Args:
        arr (list): A sorted list of comparable elements (in ascending order)
        target: The element to search for in the array
    
    Returns:
        int: The index of the target element if found, otherwise -1
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the list is not sorted
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Handle empty list case
    if not arr:
        return -1
    
    # Perform binary search
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Calculate middle index to avoid potential integer overflow
        mid = left + (right - left) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # Adjust search boundaries
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Target not found
    return -1