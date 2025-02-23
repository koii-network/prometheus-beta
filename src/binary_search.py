def binary_search(arr, target):
    """
    Perform binary search to find the first occurrence of a target in a sorted array.
    
    Args:
        arr (list): A sorted array of positive integers
        target (int): The number to search for
    
    Returns:
        int: Index of the first occurrence of target, or -1 if not found
    """
    # Check for empty array or invalid input
    if not arr or not isinstance(target, int) or target < 0:
        return -1
    
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Found a match, but continue searching left for first occurrence
            first_occurrence = mid
            right = mid - 1
        elif arr[mid] < target:
            # Target is in the right half
            left = mid + 1
        else:
            # Target is in the left half
            right = mid - 1
    
    return first_occurrence