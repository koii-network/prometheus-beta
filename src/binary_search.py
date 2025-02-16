def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target value.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The value to search for in the array
    
    Returns:
        int: Index of the target if found, otherwise -1
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is not sorted
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Empty list case
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1