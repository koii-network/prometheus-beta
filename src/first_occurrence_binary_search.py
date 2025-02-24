def find_first_occurrence(arr, target):
    """
    Find the index of the first occurrence of a target number in a sorted array 
    using binary search algorithm.

    Args:
        arr (list): A sorted array of positive integers
        target (int): The number to search for

    Returns:
        int: Index of the first occurrence of the target, or -1 if not found

    Raises:
        TypeError: If input is not a list or target is not an integer
        ValueError: If input list contains non-integer or negative values
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check if array is empty
    if not arr:
        return -1
    
    # Validate array contents
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Array must contain only positive integers")

    # Binary search for first occurrence
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # If target is found, check if it's the first occurrence
        if arr[mid] == target:
            # Check if this is the first occurrence (first element or previous element is less)
            if mid == 0 or arr[mid-1] < target:
                return mid
            # If not first occurrence, continue searching left
            right = mid - 1
        
        # Standard binary search logic
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Target not found
    return -1