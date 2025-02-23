def search_rotated_array(arr, target):
    """
    Search for a target element in a rotated sorted array.
    
    A rotated sorted array is an array that was originally sorted in ascending order,
    but then rotated around a pivot point. For example, [4,5,6,7,0,1,2] is a rotated 
    sorted array where the original sorted array was [0,1,2,4,5,6,7].
    
    Args:
        arr (list): A rotated sorted array of integers
        target (int): The element to search for
    
    Returns:
        int: The index of the target element if found, otherwise -1
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If mid is the target, return its index
        if arr[mid] == target:
            return mid
        
        # Check which half of the array is sorted
        # Left half is sorted
        if arr[left] <= arr[mid]:
            # Check if target is in the sorted left half
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Check if target is in the sorted right half
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    # Target not found
    return -1