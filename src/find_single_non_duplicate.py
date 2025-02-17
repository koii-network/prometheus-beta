def find_single_non_duplicate(arr):
    """
    Find the single element that appears only once in a sorted array 
    where all other elements appear twice.
    
    Args:
        arr (list): A sorted list of integers where all elements appear twice 
                    except for one unique element.
    
    Returns:
        int: The single non-duplicate element.
    
    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list.
    """
    # Input validation
    if arr is None:
        raise TypeError("Input cannot be None")
    
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # If only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Binary search approach for O(log n) time complexity
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Ensure mid is always the first of a pair
        if mid % 2 == 1:
            mid -= 1
        
        # Check if mid and mid+1 are same or different
        if arr[mid] == arr[mid + 1]:
            # Unique element is on the right side
            left = mid + 2
        else:
            # Unique element is on the left side or at mid
            right = mid
    
    return arr[left]