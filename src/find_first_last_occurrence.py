def find_first_last_occurrence(arr, target):
    """
    Find the first and last occurrence of a target element in a sorted array.
    
    Args:
        arr (list): A sorted list of elements
        target: The element to find
    
    Returns:
        tuple: A tuple containing (first_occurrence_index, last_occurrence_index)
               If the element is not found, returns (-1, -1)
    """
    # Check for empty array first
    if not arr:
        return (-1, -1)
    
    # Binary search for the first occurrence
    def find_first_occurrence(arr, target):
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                result = mid
                right = mid - 1  # Continue searching on the left side
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    # Binary search for the last occurrence
    def find_last_occurrence(arr, target):
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                result = mid
                left = mid + 1  # Continue searching on the right side
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    # Find first and last occurrences
    first = find_first_occurrence(arr, target)
    
    # If first occurrence not found, return (-1, -1)
    if first == -1:
        return (-1, -1)
    
    last = find_last_occurrence(arr, target)
    
    return (first, last)