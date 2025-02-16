def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    Args:
        arr (list): A sorted list of elements to search through
        target: The element to find in the array
    
    Returns:
        int: Index of the target element if found, otherwise -1
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is not sorted
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if arr != sorted(arr):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Binary search implementation
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
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