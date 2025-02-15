def find_first_last_occurrence(arr, target):
    """
    Find the first and last occurrence of a target element in a sorted array.
    
    Args:
        arr (list): A sorted array of integers
        target (int): The element to find
    
    Returns:
        tuple: A tuple containing (first_occurrence_index, last_occurrence_index)
               Returns (-1, -1) if the element is not found
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
    
    first = binary_search_first(arr, target)
    last = binary_search_last(arr, target)
    
    return (first, last)