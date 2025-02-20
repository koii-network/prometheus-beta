def binary_search(arr, target):
    """
    Perform binary search on a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers
        target (int): The number to search for
    
    Returns:
        int: Index of the first occurrence of the target, or -1 if not found
    """
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Find the first occurrence by searching left
            while mid > 0 and arr[mid-1] == target:
                mid -= 1
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return -1