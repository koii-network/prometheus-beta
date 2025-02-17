def exponential_search(arr, target):
    """
    Perform an exponential search on a sorted array.
    
    Args:
        arr (list): A sorted list of elements to search through.
        target: The element to search for.
    
    Returns:
        int: Index of the target element if found, otherwise -1.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Cannot search in an empty list")
    
    # If the first element is the target
    if arr[0] == target:
        return 0
    
    # Find range for binary search by repeated doubling
    i = 1
    while i < len(arr) and arr[i] < target:
        i *= 2
    
    # Perform binary search in the found range
    def binary_search(low, high):
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == target:
                return mid
            
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
    
    # Use binary search to find the exact location
    return binary_search(i // 2, min(i, len(arr) - 1))