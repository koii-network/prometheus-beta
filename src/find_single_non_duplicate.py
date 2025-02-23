def find_single_non_duplicate(arr):
    """
    Find the single element that appears only once in a sorted array where all other elements appear twice.
    
    Args:
        arr (list): A sorted array of integers where every element appears twice except one.
    
    Returns:
        int: The single element that appears only once.
    
    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Input validation
    if arr is None:
        raise TypeError("Input cannot be None")
    
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # If array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Binary search approach
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Ensure mid is always the first index of a potential pair
        if mid % 2 == 1:
            mid -= 1
        
        # Check if the single element is before or after mid
        if arr[mid] == arr[mid + 1]:
            # Pairs are intact, single element is after mid
            left = mid + 2
        else:
            # Potential disruption of pairs, single element might be here or before
            right = mid
    
    return arr[left]