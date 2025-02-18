def binary_search(arr, target):
    """
    Implement binary search algorithm to find the index of a target in a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
    
    Returns:
        int: Index of the target if found, -1 otherwise
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the list is not sorted
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted")
    
    # Binary search implementation
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If target is found, return its index
        if arr[mid] == target:
            return mid
        
        # If target is less than mid, search left half
        elif target < arr[mid]:
            right = mid - 1
        
        # If target is greater than mid, search right half
        else:
            left = mid + 1
    
    # Target not found
    return -1