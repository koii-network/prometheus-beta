def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target element.
    
    Args:
        arr (list): A sorted list of elements (ascending order)
        target: The element to search for
    
    Returns:
        int: Index of the target element if found, otherwise -1
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is not sorted
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if arr != sorted(arr):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Perform binary search
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target was not found
    return -1