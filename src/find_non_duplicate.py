def find_single_non_duplicate(arr):
    """
    Find the single non-duplicate element in a sorted array.
    
    In a sorted array where every element appears twice except for one element,
    this function returns the single non-duplicate element.
    
    Args:
        arr (List[int]): A sorted array where all elements appear twice except one.
    
    Returns:
        int: The single non-duplicate element.
    
    Raises:
        ValueError: If the input array is empty or None.
        ValueError: If no single non-duplicate element is found.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Examples:
        >>> find_single_non_duplicate([1, 1, 2, 3, 3, 4, 4])
        2
        >>> find_single_non_duplicate([1, 1, 2, 2, 3, 3, 4, 5, 5])
        4
    """
    # Check for invalid input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # If array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Binary search approach
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Handle first and last element special cases
        if left == right:
            return arr[left]
        
        # Check mid and its neighbors
        mid = left + (right - left) // 2
        
        # Check if mid is the unique element
        if mid % 2 == 1:
            mid -= 1
        
        # If mid and next element are same, unique element is on right side
        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        # Unique element is on left side or at mid
        else:
            right = mid
    
    # This should not be reached if input is valid
    raise ValueError("No single non-duplicate element found")