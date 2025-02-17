def exponential_search(arr, target):
    """
    Perform exponential search on a sorted array.
    
    Args:
        arr (list): A sorted list of elements to search through
        target: The element to search for
    
    Returns:
        int: Index of the target element if found, else -1
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the list is empty
    """
    # Check input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Cannot search in an empty list")
    
    # If first element is the target
    if arr[0] == target:
        return 0
    
    # Find range for binary search by repeated doubling
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Perform binary search in the found range
    return binary_search(arr, target, i//2, min(i, len(arr)-1))

def binary_search(arr, target, left, right):
    """
    Perform binary search in a specified range.
    
    Args:
        arr (list): Sorted list to search
        target: Element to find
        left (int): Left boundary of search range
        right (int): Right boundary of search range
    
    Returns:
        int: Index of target if found, else -1
    """
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1