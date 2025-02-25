def find_single_non_duplicate(arr):
    """
    Find the single element that appears only once in a sorted array.
    
    Args:
        arr (list): A sorted array where every element appears twice except for one unique element.
    
    Returns:
        int: The single non-duplicate element.
    
    Raises:
        ValueError: If the input array is invalid (empty or None).
        ValueError: If no single non-duplicate element is found.
    """
    # Input validation
    if not arr or len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # If array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Check first element
    if arr[0] != arr[1]:
        return arr[0]
    
    # Check last element
    if arr[-1] != arr[-2]:
        return arr[-1]
    
    # Binary search for unique element
    left, right = 1, len(arr) - 2
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the unique element
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        
        # Determine which side to search
        # Use mid's index parity to decide search direction
        if mid % 2 == 1:
            if arr[mid] == arr[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[mid] == arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
    
    raise ValueError("No single non-duplicate element found")