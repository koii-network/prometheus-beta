def binary_search(arr, target):
    """
    Perform an efficient binary search to find the index of a target element in a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements in ascending order
        target: The element to search for in the array
    
    Returns:
        int: Index of the target element if found, -1 otherwise
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is not sorted
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted (optional, but adds robustness)
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Standard binary search implementation
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Prevent potential integer overflow
        mid = left + (right - left) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # Decide which half to search
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Target not found
    return -1