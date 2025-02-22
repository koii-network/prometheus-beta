def find_single_non_duplicate(arr):
    """
    Find the single non-duplicate element in a sorted array.
    
    In a sorted array where every element appears twice except for one element,
    this function returns the single element that appears only once.
    
    Args:
        arr (list): A sorted list of integers where all elements are duplicates
                    except for one unique element.
    
    Returns:
        int: The single non-duplicate element.
    
    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list.
    """
    # Validate input
    if arr is None:
        raise TypeError("Input cannot be None")
    
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # If only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Binary search approach
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Ensure mid is always the first index of a pair
        if mid % 2 == 1:
            mid -= 1
        
        # If mid and mid+1 are same, unique element is on right side
        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        else:
            # Unique element is on left side or at mid
            right = mid
    
    return arr[left]