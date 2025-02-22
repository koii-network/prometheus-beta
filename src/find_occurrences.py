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
    def binary_search_first(arr, target):
        left, right = 0, len(arr) - 1
        first_occurrence = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                first_occurrence = mid
                right = mid - 1  # Continue searching in the left half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return first_occurrence
    
    def binary_search_last(arr, target):
        left, right = 0, len(arr) - 1
        last_occurrence = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                last_occurrence = mid
                left = mid + 1  # Continue searching in the right half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return last_occurrence
    
    # Handle empty array case
    if not arr:
        return (-1, -1)
    
    first = binary_search_first(arr, target)
    
    # If target is not found, return (-1, -1)
    if first == -1:
        return (-1, -1)
    
    last = binary_search_last(arr, target)
    
    return (first, last)