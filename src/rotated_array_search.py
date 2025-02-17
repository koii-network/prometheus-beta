def search_rotated_array(arr, target):
    """
    Search for a target element in a rotated sorted array.
    
    Args:
        arr (list): A rotated sorted array of unique integers
        target (int): The element to search for
    
    Returns:
        int: Index of the target element, or -1 if not found
    """
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If mid is the target, return its index
        if arr[mid] == target:
            return mid
        
        # Check which half is sorted
        if arr[left] <= arr[mid]:
            # Left half is sorted
            if arr[left] <= target < arr[mid]:
                # Target is in the left sorted half
                right = mid - 1
            else:
                # Target is in the right half
                left = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[right]:
                # Target is in the right sorted half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1
    
    return -1