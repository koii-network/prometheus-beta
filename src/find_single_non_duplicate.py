def find_single_non_duplicate(arr):
    """
    Find the single element that appears only once in a sorted array 
    where all other elements appear exactly twice.
    
    Args:
        arr (list): A sorted list of integers
    
    Returns:
        int: The single element that appears only once
    
    Raises:
        ValueError: If the input array is empty or None
        TypeError: If the input is not a list
    """
    # Input validation
    if arr is None:
        raise TypeError("Input cannot be None")
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # If array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Binary search approach
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Ensure mid is even 
        if mid % 2 == 1:
            mid -= 1
        
        # Check if the single element is on the left or right side
        if arr[mid] == arr[mid + 1]:
            # If match found, single element is on the right side
            left = mid + 2
        else:
            # If no match, single element is on the left side or at mid
            right = mid
    
    return arr[left]