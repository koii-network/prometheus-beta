def find_single_non_duplicate(arr):
    """
    Find the single element that appears only once in a sorted array.
    
    Args:
        arr (list): A sorted array where all elements except one appear twice.
    
    Returns:
        int: The single non-duplicate element.
    
    Raises:
        ValueError: If the input array is empty or None.
        ValueError: If no single non-duplicate element exists.
    """
    # Check for invalid input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # If array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Check first and last elements as special cases
    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]
    
    # Binary search approach
    left, right = 1, len(arr) - 2
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the unique element
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        
        # Determine which half to search
        # If mid is even and matches next, or 
        # if mid is odd and matches previous, search right half
        if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or \
           (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
            left = mid + 1
        else:
            right = mid - 1
    
    # If no single element is found
    raise ValueError("No single non-duplicate element found")