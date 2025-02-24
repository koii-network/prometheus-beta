def search_rotated_array(arr, target):
    """
    Search for a target element in a rotated sorted array.
    
    A rotated sorted array is an array that was originally sorted in ascending order,
    but has been rotated around a pivot point. For example, [4,5,6,7,0,1,2] is a 
    rotated version of [0,1,2,4,5,6,7].
    
    Args:
        arr (list): A rotated sorted array of unique integers
        target (int): The element to search for
    
    Returns:
        int: The index of the target element if found, otherwise -1
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Raises:
        TypeError: If input is not a list or target is not an integer
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Handle empty array
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If mid element is the target, return its index
        if arr[mid] == target:
            return mid
        
        # Check which half is sorted
        # Left half is sorted
        if arr[left] <= arr[mid]:
            # Check if target is in the left sorted half
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Check if target is in the right sorted half
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    # Target not found
    return -1