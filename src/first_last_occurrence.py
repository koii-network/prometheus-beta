def find_first_last_occurrence(arr, target):
    """
    Find the first and last occurrence of a target element in a sorted array.
    
    Args:
        arr (list): A sorted array of elements
        target: The element to find in the array
    
    Returns:
        tuple: A tuple containing (first_index, last_index)
               If the target is not found, returns (-1, -1)
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def binary_search_first(arr, target):
        """Find the first occurrence of the target."""
        left, right = 0, len(arr) - 1
        first_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                first_index = mid
                # Continue searching in the left half
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return first_index
    
    def binary_search_last(arr, target):
        """Find the last occurrence of the target."""
        left, right = 0, len(arr) - 1
        last_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                last_index = mid
                # Continue searching in the right half
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return last_index
    
    # Handle empty array case
    if not arr:
        return (-1, -1)
    
    # Find first and last occurrences
    first = binary_search_first(arr, target)
    last = binary_search_last(arr, target)
    
    return (first, last)