def find_single_non_duplicate(arr):
    """
    Find the single element in a sorted array that appears only once.
    All other elements appear exactly twice.
    
    Args:
        arr (list): A sorted array where all elements except one appear twice.
    
    Returns:
        int: The single non-duplicate element.
    
    Raises:
        ValueError: If the input array is empty or None.
        ValueError: If no single non-duplicate element is found.
    """
    # Check for invalid input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # If array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Check first and last elements separately
    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]
    
    # Binary search to find the single element
    left, right = 1, len(arr) - 2
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the unique element
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        
        # Determine which side to continue searching
        # If mid is on the left half, the unique element is on this side 
        # if the first pair is broken
        if (mid % 2 == 1 and arr[mid] == arr[mid-1]) or \
           (mid % 2 == 0 and arr[mid] == arr[mid+1]):
            right = mid - 1
        else:
            left = mid + 1
    
    # If no single element found
    raise ValueError("No single non-duplicate element found")