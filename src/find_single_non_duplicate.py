def find_single_non_duplicate(arr):
    """
    Find the single element in a sorted array that appears only once.
    
    Args:
        arr (list): A sorted array of integers where all elements appear twice 
                    except for one element which appears only once.
    
    Returns:
        int: The single non-duplicate element.
    
    Raises:
        ValueError: If the input array is None, empty, or invalid.
    """
    # Check for invalid input
    if not arr or not isinstance(arr, list):
        raise ValueError("Input must be a non-empty list")
    
    # If array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Binary search approach
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Check if first half has the single element
        mid = left + (right - left) // 2
        
        # Ensure mid is at the first occurrence of a pair
        if mid % 2 == 1:
            mid -= 1
        
        # If elements at mid and mid+1 are different, single element is in left half
        if mid + 1 < len(arr) and arr[mid] != arr[mid + 1]:
            return arr[mid]
        
        # If elements at mid and mid+1 are same, single element is in right half
        if mid + 1 < len(arr) and arr[mid] == arr[mid + 1]:
            left = mid + 2
        else:
            right = mid - 1
    
    # If no element found (shouldn't happen for valid input)
    raise ValueError("No single non-duplicate element found")