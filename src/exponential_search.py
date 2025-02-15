def exponential_search(arr, target):
    """
    Perform exponential search on a sorted array.
    
    Args:
        arr (list): A sorted list of elements to search through.
        target: The element to search for.
    
    Returns:
        int: Index of the target element if found, otherwise -1.
    
    Raises:
        TypeError: If input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty list case
    if not arr:
        return -1
    
    # If first element is the target
    if arr[0] == target:
        return 0
    
    # Find range for binary search by repeated doubling
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Perform binary search in the found range
    def binary_search(arr, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid
            
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    # Return binary search result in the found range
    return binary_search(arr, i//2, min(i, len(arr)-1), target)