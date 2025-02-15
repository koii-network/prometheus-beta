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
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Ensure mid is always looking at first occurrence of the pair
        if mid % 2 == 1:
            mid -= 1
        
        # Check if current pair is broken
        if arr[mid] != arr[mid+1]:
            return arr[mid]
        
        # Determine search direction
        if mid < len(arr) - 2:
            # If pairs to the left of mid are complete, search right
            if arr[mid] == arr[mid+1]:
                left = mid + 2
            else:
                right = mid - 2
        else:
            break
    
    # If no single element found
    raise ValueError("No single non-duplicate element found")