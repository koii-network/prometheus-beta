def search_rotated_sorted_array(arr, target):
    """
    Search for a target element in a rotated sorted array.
    
    Args:
        arr (list): A rotated sorted array of distinct integers
        target (int): The element to search for
    
    Returns:
        int: Index of the target element, or -1 if not found
    
    Time complexity: O(log n)
    Space complexity: O(1)
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
        # Left half is sorted
        if arr[left] <= arr[mid]:
            # Target is in the left sorted half
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # Right half is sorted
        else:
            # Target is in the right sorted half
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1