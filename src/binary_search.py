def find_first_occurrence(arr, target):
    """
    Find the index of the first occurrence of a target number in a sorted array 
    using binary search algorithm.
    
    Args:
        arr (list): A sorted array of positive integers
        target (int): The number to find
    
    Returns:
        int: Index of the first occurrence of target, or -1 if not found
    """
    # Handle empty array case
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If target is found, check if it's the first occurrence
        if arr[mid] == target:
            # If this is the first element or the previous element is less than target
            if mid == 0 or arr[mid-1] < target:
                return mid
            # Otherwise, continue searching in the left half
            right = mid - 1
        
        # If target is less than mid element, search left half
        elif target < arr[mid]:
            right = mid - 1
        
        # If target is greater than mid element, search right half
        else:
            left = mid + 1
    
    # Target not found
    return -1